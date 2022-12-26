from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator, Set, List, Optional, Callable, Iterable, Generator, Dict, Tuple

import logging
logging.basicConfig()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@dataclass(frozen=True)
class Position:
    x: int = 0
    y: int = 0

    def __add__(self, other: Position):
        return Position(self.x + other.x, self.y + other.y)

    def blow(self, direction):
        if direction == '<':
            return self + Position(-1, 0)

        if direction == '>':
            return self + Position(1, 0)

        raise Exception(f'Unknown direction: {direction}')

    def drop(self):
        return Position(self.x, self.y-1)


rocks = """
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""


@dataclass()
class Rock:
    # note: blocked positions go downwards.
    # Cave positions go upwards.
    blocked: Set[Position]
    position: Position = field(default_factory=Position)

    def move(self, vector: Position, blocked: Set[Position]) -> bool:
        offset_position = self.position + vector
        if self.is_blocked(blocked, offset_position):
            return False

        self.position = offset_position
        return True

    def blow(self, direction: str, blocked: Set[Position]) -> bool:
        offsets = {
            '<': Position(-1, 0),
            '>': Position(1, 0)
        }
        vector = offsets[direction]
        return self.move(vector, blocked)

    def drop(self, blocked: Set[Position]) -> bool:
        vector = Position(0, -1)
        return self.move(vector, blocked)

    def is_blocked(self, blocked: Set[Position],
                   offset_position: Optional[Position] = None) -> bool:

        for position in self.blocked_positions(offset_position):

            if position.x < 0 or position.x > 6:
                return True

            if position.y < 1:
                return True

            if position in blocked:
                return True
        return False

    def blocked_positions(self,
                          offset_position: Optional[Position] = None
                          ) -> Set[Position]:
        if offset_position is None:
            offset_position = self.position

        return {b + offset_position for b in self.blocked}


@dataclass
class Rocks:
    rock_data: str = rocks
    rocks: List[Rock] = field(default_factory=list)
    i: int = 0

    def __post_init__(self):
        rows = []
        for line in self.rock_data.split('\n'):
            if line == '':
                self.add_rock(rows)
                rows = []
            else:
                rows.append(line)
        self.add_rock(rows)

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Rock:
        ret_i = self.i
        self.i = (self.i + 1) % len(self.rocks)
        return Rock(blocked=self.rocks[ret_i].blocked)

    def add_rock(self, rows: List[str]):
        if len(rows) == 0:
            return
        rock_set: Set[Position] = set()
        # lines go down, but we want our rock positions to go up
        # so reverse the rows
        for y, row in enumerate(reversed(rows)):
            for x, char in enumerate(row):
                if char == '#':
                    rock_set.add(Position(x, y))
        self.rocks.append(Rock(rock_set))


@dataclass
class Wind:
    pattern: str
    i: int = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> str:
        ret_i = self.i
        self.i = (self.i + 1) % len(self.pattern)
        return self.pattern[ret_i]


ProgressFunc = Callable[[Iterable[int], int], Generator]


@dataclass(frozen=True)
class CaveState:
    wind_i: int
    rock_i: int
    blocked: frozenset


@dataclass
class Cave:
    wind_filename: str
    blocked: Set[Position] = field(default_factory=set)
    rocks: Rocks = field(default_factory=Rocks)
    count: int = 0
    max_y: int = 0
    collapsed: int = 0

    wind: Wind = field(init=False)

    def __post_init__(self):
        with open(self.wind_filename) as f:
            line = f.read().strip()
            self.wind = Wind(line)

    def drop_rocks(self, num_drops: int = 1,
                   progress: Optional[ProgressFunc] = None):

        seen_states: Dict[CaveState, Tuple[int, int]] = {}

        if progress is not None:
            with progress(length=num_drops) as bar:
                i = 0
                while i < num_drops:
                    if i % 1000 == 0:
                        logger.info(f'Dropped {i} rocks')
                    self.drop_rock()
                    state = CaveState(self.wind.i, self.rocks.i,
                                      frozenset(self.blocked))
                    if state in seen_states:
                        previous_i, previous_max_y = seen_states[state]
                        states_since = i - previous_i
                        max_y_increased = (
                            self.max_y + self.collapsed) - previous_max_y

                        logger.info(f'{states_since} rocks ago, the height '
                                    f'has increased by {max_y_increased}')

                        # fast forward
                        iterations_needed = (num_drops - i) // states_since
                        logger.info(
                            f'Need another {iterations_needed} iterations')
                        i += iterations_needed * states_since
                        self.collapsed += iterations_needed * max_y_increased
                        bar.update(iterations_needed * states_since)
                        seen_states.clear()

                    seen_states[state] = (i, self.max_y + self.collapsed)

                    i += 1

        else:
            for i in range(num_drops):
                self.drop_rock()

    def drop_rock(self):
        rock: Rock = next(self.rocks)
        rock.position = self.spawn_position(rock)
        while True:
            # blow

            direction = next(self.wind)
            rock.blow(direction, self.blocked)

            # drop
            rock_was_dropped = rock.drop(self.blocked)
            if not rock_was_dropped:
                break

        self.count += 1
        blocked_positions = rock.blocked_positions()
        self.blocked |= blocked_positions
        max_blocked_position = max(
            [position.y for position in blocked_positions])

        if max_blocked_position > self.max_y:
            self.max_y = max_blocked_position

        # if we have a whole blocked row, then we can make that the new floor.
        blocked_row = self.find_blocked_row()
        if blocked_row > 0:
            self.collapse_rows(blocked_row)

    def collapse_rows(self, y: int):
        collapsed: Set[Position] = set()
        vector = Position(0, -y)
        for position in self.blocked:
            if position.y <= y:
                continue
            collapsed.add(position + vector)
        self.collapsed += y
        self.max_y -= y
        self.blocked = collapsed
        # logger.info(f'Collapsing rows <= {y} [total so far = {self.collapsed}')

    def is_row_blocked(self, y: int) -> bool:
        for x in range(7):
            if Position(x, y) not in self.blocked:
                return False
        return True

    def find_blocked_row(self) -> int:
        for y in range(self.max_y):
            if self.is_row_blocked(y):
                return y
        return 0

    def spawn_position(self, rock: Rock) -> Position:
        """Return the top-left position of the newly-spawned rock.
s
        Args:
            rock (Rock): the newly-spawned rock.

        Returns:
            Position: the top-left position
        """
        x = 2
        y = self.max_y + 4
        return Position(x, y)

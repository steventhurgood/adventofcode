from __future__ import annotations

import heapq
from dataclasses import dataclass, field
from typing import List, Mapping, Optional, Sequence, Set, TextIO

from absl import logging


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def adjacent(self) -> Sequence[Position]:
        return [
            Position(self.x, self.y+1),  # North
            Position(self.x+1, self.y),  # East
            Position(self.x, self.y-1),  # South
            Position(self.x-1, self.y),  # West
        ]

    def char_to(self, other: Position, backwards: bool = False) -> str:
        """Returns the character going from this position to another position

        Args:
            other (Position): the position towards which we are moving
            backwards (bool, optional): Whether or not we are moving backwards

        Returns:
            str: _description_
        """
        x_diff = self.x - other.x
        y_diff = self.y - other.y

        if backwards:
            x_diff = -x_diff
            y_diff = -y_diff

        chars = {
            (1, 0): '>',
            (-1, 0): '<',
            (0, 1): 'v',
            (0, -1): '^',
        }

        return chars.get((x_diff, y_diff), 'X')


@dataclass(order=True)
class ReachablePosition:
    steps: int

    position: Position = field(compare=False)
    previous: Optional[ReachablePosition] = field(default=None, compare=False)


class Heights:
    rows: List[List[int]]
    end: Position
    start: Position

    width: int = 0
    height: int = 0
    steps: int = 0

    path: Optional[ReachablePosition] = None

    def __init__(self, input: TextIO, *args, **kwargs):
        rows = []
        self.start = None
        self.end = None

        for y, line in enumerate(input):
            row = []
            for x, char in enumerate(line.strip()):
                if char == 'S':
                    self.start = Position(x, y)
                    char = 'a'
                if char == 'E':
                    self.end = Position(x, y)
                    char = 'z'

                height = ord(char) - ord('a')
                row.append(height)
            rows.append(row)

        if self.start is None:
            raise Exception('No start position found')

        if self.end is None:
            raise Exception('No end position found')

        self.height = len(rows)
        if self.height > 0:
            self.width = len(rows[0])
        logging.info(
            f'Assembling height map {self.width} x {self.height} ({self.width * self.height})')
        self.rows = rows

    def build_path_map(self, start: ReachablePosition, backwards: bool = False) -> Mapping[Position, str]:
        """build_path_map builds a map of positions to the ascii character representing the path

        Args:
            start (ReachablePosition): The start of the chain of positions
            backwards (bool, optional): Which direction we are traversing the path
        """

        if start.previous is None:
            return {}

        char = start.previous.position.char_to(start.position, backwards)
        path = {start.previous.position: char}

        path.update(self.build_path_map(start.previous, backwards))
        return path

    def __str__(self) -> str:
        path: Mapping[Position, str] = {}

        if self.path is not None:
            path = self.build_path_map(self.path)

        rows = []
        for y, row in enumerate(self.rows):
            chars = []
            for x, height in enumerate(row):
                position = Position(x, y)
                char = chr(height+ord('a'))
                if position in path:
                    char = path[position]
                if self.start == position:
                    char = 'S'
                if self.end == position:
                    char = 'E'

                chars.append(char)
            rows.append(''.join(chars))
        return '\n'.join(rows)

    def find_shortest_path_to_a(self):
        """Find the shortest path to any position at level 0 ('a')
        """

        reached_from_end: List[ReachablePosition] = []  # heap
        heapq.heappush(reached_from_end,  ReachablePosition(0, self.end))

        visited_from_end: Mapping[Position, ReachablePosition] = {}

        considered: int = 0

        while True:
            current_from_end = reached_from_end[0]
            reached_from_end = reached_from_end[1:]

            if current_from_end.position in visited_from_end:
                # we have already found a shorted path to this position
                continue

            visited_from_end[current_from_end.position] = current_from_end

            if self.height_at(current_from_end.position) == 0:
                logging.info(
                    f'Found new path starting at {current_from_end.position} of {current_from_end.steps} steps')
                self.steps = current_from_end.steps
                self.path = current_from_end
                self.start = current_from_end.position
                break

            next_steps = self.next_steps(
                current_from_end.position, visited_from_end, climbing=False)

            for step in next_steps:
                heapq.heappush(reached_from_end, ReachablePosition(
                    current_from_end.steps+1, step, current_from_end))

    def find_path(self):
        """Start navigating from Start to End
        """
        # reached is the list of positions we've reached so far,
        # ordered by the number of steps taken to get there.
        reached_from_start: List[Tuple[int, Position]] = [(0, self.start)]
        reached_from_end: List[Tuple[int, Position]] = [(0, self.end)]

        visited_from_start: Mapping[Position, int] = {}  # {self.start: 0}
        visited_from_end: Mapping[Position, int] = {}  # {self.end: 0}

        considered: int = 0

        while True:
            # consider the position that can be reached with the fewest
            # steps so far
            steps_from_start, current_from_start = reached_from_start[0]
            reached_from_start = reached_from_start[1:]
            if current_from_start in visited_from_start:
                continue
            visited_from_start[current_from_start] = steps_from_start

            if current_from_start in visited_from_end:
                #
                self.steps = steps_from_start + \
                    visited_from_end[current_from_start]
                break

            next_steps = self.next_steps(
                current_from_start,
                visited_from_start,
                climbing=True)

            for step in next_steps:
                reached_from_start.append((steps_from_start+1, step))

            # only sort on the distance
            reached_from_start.sort(key=lambda x: x[0])

            steps_from_end, current_from_end = reached_from_end[0]
            reached_from_end = reached_from_end[1:]
            if current_from_end in visited_from_end:
                continue
            visited_from_end[current_from_end] = steps_from_end

            if current_from_end in visited_from_start:
                self.steps = steps_from_end + \
                    visited_from_start[current_from_end]
                break

            next_steps = self.next_steps(
                current_from_end,
                visited_from_end,
                climbing=False)
            for step in next_steps:
                reached_from_end.append((steps_from_end+1, step))

            reached_from_end.sort(key=lambda x: x[0])

            if len(reached_from_start) == 0 or len(reached_from_end) == 0:
                # we have exhausted our candidates and still not reached the end
                raise Exception(
                    f'End {self.end} is unreachable from {self.start}')

            considered += 1
            if considered % 100 == 0:
                logging.info(
                    f'Considered {considered*2} positions with {len(reached_from_start)} positions reachable from the start and {len(reached_from_end)} positions reachable from the end')

    def height_at(self, position: Position) -> int:
        return self.rows[position.y][position.x]

    def next_steps(self, current: Position, visited: Mapping[Position, int], climbing: bool = True) -> Sequence[Position]:
        candidates = []

        for position in current.adjacent():
            first = current
            second = position
            if not climbing:
                first, second = second, first

            if (
                position.x >= 0
                and
                position.x < self.width
                and
                position.y >= 0
                and
                position.y < self.height
                and
                self.height_at(second) - self.height_at(first) <= 1
                and
                position not in visited
            ):
                candidates.append(position)
        return candidates

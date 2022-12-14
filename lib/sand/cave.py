from __future__ import annotations

from dataclasses import dataclass
from typing import List, Set, Optional, Tuple
from collections.abc import Iterable

import antlr4

from lib.sand.grammar.CaveLexer import CaveLexer
from lib.sand.grammar.CaveParser import CaveParser
from lib.sand.grammar.CaveVisitor import CaveVisitor

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


@dataclass(frozen=True)
class Point:
    x: int
    y: int


Line = List[Point]


@dataclass
class CaveBuilder(CaveVisitor):
    input_filename: str

    def build(self, has_floor: bool = False) -> Cave:
        data = antlr4.FileStream(self.input_filename)
        lexer = CaveLexer(data)
        stream = antlr4.CommonTokenStream(lexer)
        parser = CaveParser(stream)

        rocks = self.visit(parser.cave())
        return Cave.from_rocks(rocks, has_floor)

    def visitCave(self, ctx) -> List[Line]:
        rocks: List[Line] = []
        # every other child is a rock: 0, 2, 4, ...
        for child in ctx.children:
            if not isinstance(child, CaveParser.RockContext):
                continue
            rock = self.visit(child)
            rocks.append(rock)
        return rocks

    def visitRock(self, ctx) -> Line:
        points: Line = []
        # every other child is a pair
        for i in range(0, len(ctx.children), 2):
            child = ctx.children[i]
            pair = self.visit(child)
            points.append(pair)
        return points

    def visitPair(self, ctx) -> Point:
        x = self.visit(ctx.x())
        y = self.visit(ctx.y())
        return Point(x, y)

    def visitX(self, ctx) -> int:
        return self.visit(ctx.number())

    def visitY(self, ctx) -> int:
        return self.visit(ctx.number())

    def visitNumber(self, ctx) -> int:
        return int(ctx.getText())


@ dataclass
class Cave:
    rocks: Set[Point]
    sand: Set[Point]

    rock_min: Point
    rock_max: Point

    cycle_count: int = 0
    has_floor: bool = False

    @ classmethod
    def from_rocks(cls, lines: List[Line], has_floor: bool = False) -> Cave:

        # render lines
        rocks: Set[Point] = set()

        for line in lines:
            for i in range(len(line)-1):
                from_point: Point = line[i]
                to_point: Point = line[i+1]
                cls.render_line(from_point, to_point, rocks)

        rock_min, rock_max = cls.find_extents(rocks)
        return Cave(
            rocks=rocks,
            sand=set(),
            rock_min=rock_min,
            rock_max=rock_max,
            has_floor=has_floor
        )

    @classmethod
    def render_line(cls, from_point: Point, to_point: Point, rocks: Set[Point]):
        x_delta = to_point.x - from_point.x
        y_delta = to_point.y - from_point.y

        x_diff = sign(x_delta)
        y_diff = sign(y_delta)

        steps = max(abs(x_delta), abs(y_delta))

        current = from_point
        for _ in range(steps+1):
            rocks.add(current)
            current = Point(current.x + x_diff, current.y + y_diff)

    @classmethod
    def find_extents(cls, points: Iterable[Point]) -> Tuple[Point, Point]:
        min: Optional[Point] = None
        max: Optional[Point] = None

        for point in points:
            if min is None:
                min = point
            if max is None:
                max = point
            if point.x < min.x:
                min = Point(point.x, min.y)
            if point.x > max.x:
                max = Point(point.x, max.y)
            if point.y < min.y:
                min = Point(min.x, point.y)
            if point.y > max.y:
                max = Point(max.x, point.y)
        return (min, max)

    @classmethod
    def optional_min(cls, a: Optional[Point], b: Optional[Point]) -> Point:
        if a is None and b is None:
            raise Exception('Cannot find min of two None Points')

        if a is None:
            return b

        if b is None:
            return a

        return Point(min(a.x, b.x), min(a.y, b.y))

    @classmethod
    def optional_max(cls, a: Optional[Point], b: Optional[Point]) -> Point:
        if a is None and b is None:
            raise Exception('Cannot find min of two None Points')

        if a is None:
            return b

        if b is None:
            return a

        return Point(max(a.x, b.x), min(a.y, b.y))

    def __str__(self) -> str:
        rows = []
        sand_min, sand_max = Cave.find_extents(self.sand)

        render_min: Point = Cave.optional_min(self.rock_min, sand_min)
        render_max: Point = Cave.optional_max(self.rock_max, sand_max)

        # clamp min y at 0
        render_min = Point(render_min.x, min(render_min.y, 0))

        # max max include rock_max.y + 2
        render_max = Point(render_max.x, max(render_max.y, self.rock_max.y+2))

        for y in range(render_min.y, render_max.y+1):
            row: List[str] = []
            for x in range(render_min.x, render_max.x+1):
                point = Point(x, y)
                if point in self.rocks:
                    row.append('#')
                    continue
                if point in self.sand:
                    row.append('o')
                    continue
                row.append('.')
            rows.append(''.join(row))

        return '\n'.join(rows)

    def drop_sand(self, position: Point):
        self.sand.add(position)

    def out_of_bounds(self, position: Point) -> bool:
        if self.has_floor:
            return False

        return (position.y > self.rock_max.y
                or position.x < self.rock_min.x
                or position.x > self.rock_max.x)

    def blocked(self, position: Point) -> bool:
        blocked_by_rock = position in self.rocks
        blocked_by_sand = position in self.sand
        blocked_by_bedrock = position.y >= self.rock_max.y + 2

        return blocked_by_rock or blocked_by_sand or blocked_by_bedrock

    def simulate(self, max_cycles: Optional[int] = None) -> bool:
        """Simulate one cycle of sand entering the cave

        Returns:
            bool: True if the sand came to rest in the cave, False if it fell out.
        """
        if max_cycles is not None and self.cycle_count >= max_cycles:
            raise Exception('max cycle count {max_cycles} reached')
        current = Point(500, 0)

        directions = [
            Point(0, 1),  # down
            Point(-1, 1),  # down-left
            Point(1, 1),  # down-right
        ]

        while True:
            # attempt to fall down.
            moved = False

            for direction in directions:
                next_step = Point(current.x+direction.x, current.y+direction.y)

                if self.out_of_bounds(next_step):
                    return False

                if self.blocked(next_step):
                    continue

                current = next_step
                moved = True
                break

            if not moved:
                self.drop_sand(current)
                self.cycle_count += 1
                if current == Point(500, 0):
                    # we have not moved
                    return False
                return True


def sign(a: int) -> int:
    if a == 0:
        return 0
    if a < 0:
        return -1
    if a > 0:
        return 1

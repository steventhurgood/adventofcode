from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

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

    def build(self) -> Cave:
        data = antlr4.FileStream(self.input_filename)
        lexer = CaveLexer(data)
        stream = antlr4.CommonTokenStream(lexer)
        parser = CaveParser(stream)

        return self.visit(parser.cave())

    def visitCave(self, ctx) -> Cave:
        rocks: List[Line] = []
        # every other child is a rock: 0, 2, 4, ...
        for child in ctx.children:
            if not isinstance(child, CaveParser.RockContext):
                continue
            rock = self.visit(child)
            rocks.append(rock)
        return Cave.from_rocks(rocks)

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
    rows: List[List[str]]

    min: Point
    max: Point

    width: int
    height: int

    cycle_count: int = 0

    @ classmethod
    def from_rocks(cls, rocks: List[Lines]) -> Cave:
        # calculate extents
        # minimum y must always include y=0
        min: Point = Point(rocks[0][0].x, 0)
        max: Point = rocks[0][0]

        for line in rocks:
            for point in line:
                if point.x < min.x:
                    min = Point(point.x, min.y)
                if point.y < min.y:
                    min = Point(min.x, point.y)
                if point.x > max.x:
                    max = Point(point.x, max.y)
                if point.y > max.y:
                    max = Point(max.x, point.y)
        width = max.x - min.x
        height = max.y - min.y

        # build empty cave
        rows: List[str] = []
        for _ in range(height+1):
            rows.append(['.'] * (width+1))
        # render lines

        for line in rocks:
            for i in range(len(line)-1):
                from_point: Point = line[i]
                to_point: Point = line[i+1]
                cls.render_line(from_point, to_point, min, rows)

        return Cave(
            rows=rows,
            min=min,
            max=max,
            width=width,
            height=height
        )

    @classmethod
    def render_line(cls, from_point: Point, to_point: Point, min: Point, rows: List[List[str]]):
        x_delta = to_point.x - from_point.x
        y_delta = to_point.y - from_point.y

        x_diff = sign(x_delta)
        y_diff = sign(y_delta)

        steps = max(abs(x_delta), abs(y_delta))

        current = from_point
        for _ in range(steps+1):
            rows[current.y-min.y][current.x-min.x] = '#'
            current = Point(current.x + x_diff, current.y + y_diff)

    def __str__(self) -> str:
        return '\n'.join([''.join(row) for row in self.rows])

    def simulate(self) -> bool:
        """Simulate one cycle of sand entering the cave

        Returns:
            bool: True if the sand came to rest in the cave, False if it fell out.
        """
        return False


def sign(a: int) -> int:
    if a == 0:
        return 0
    if a < 0:
        return -1
    if a > 0:
        return 1

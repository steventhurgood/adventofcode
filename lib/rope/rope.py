from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Mapping, Set, TextIO, Tuple, List

from absl import logging


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: Point):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point):
        return Point(self.x-other.x, self.y-other.y)


@dataclass
class Rope:
    points: List[Point]
    visited: List[Set[Point]]

    tailmoves: Mapping[Point, Point] = field(default_factory=dict)

    offsets: ClassVar[Mapping[str, Point]] = {
        'U': Point(0, 1),
        'D': Point(0, -1),
        'L': Point(-1, 0),
        'R': Point(1, 0)
    }

    def initialize_tailmoves(self):
        self.tailmoves = {}

        for y in range(-1, 2):
            for x in range(-1, 2):
                # if we're touching, we don't have to move:
                self.tailmoves[Point(x, y)] = Point(0, 0)

        # horizontal moves
        self.tailmoves[Point(-2, 0)] = Point(-1, 0)
        self.tailmoves[Point(2, 0)] = Point(1, 0)

        # vertical moves
        self.tailmoves[Point(0, -2)] = Point(0, -1)
        self.tailmoves[Point(0, 2)] = Point(0, 1)

        # diagonal moves
        self.tailmoves[Point(-2, -2)] = Point(-1, -1)
        self.tailmoves[Point(-2, -1)] = Point(-1, -1)
        self.tailmoves[Point(2, -1)] = Point(1, -1)
        self.tailmoves[Point(2, -2)] = Point(1, -1)

        self.tailmoves[Point(-2, 2)] = Point(-1, 1)
        self.tailmoves[Point(-2, 1)] = Point(-1, 1)
        self.tailmoves[Point(2, 1)] = Point(1, 1)
        self.tailmoves[Point(2, 2)] = Point(1, 1)

        self.tailmoves[Point(-1, -2)] = Point(-1, -1)
        self.tailmoves[Point(-1, 2)] = Point(-1, 1)

        self.tailmoves[Point(1, -2)] = Point(1, -1)
        self.tailmoves[Point(1, 2)] = Point(1, 1)

    def __init__(self, num_points: int = 2):
        self.visited = [set([Point(0, 0)]) for _ in range(num_points)]
        self.points = [Point(0, 0) for _ in range(num_points)]

        self.initialize_tailmoves()

    def move(self, direction: str, count: int):
        offset = self.offsets[direction]
        for _ in range(count):
            new_head = self.points[0] + offset
            logging.info(f'Moving head from {self.points[0]} to {new_head}')
            self.points[0] = new_head
            self.visited[0].add(new_head)

            for segment in range(1, len(self.points)):
                segment_diff = self.points[segment-1] - self.points[segment]
                segment_move = self.tailmoves[segment_diff]
                new_segment = self.points[segment] + segment_move
                logging.info(
                    f'Moving segment {segment} from {self.points[segment]} to {new_segment}')
                self.points[segment] = new_segment
                self.visited[segment].add(new_segment)

    def process(self, input: TextIO):
        for line in input:
            parts = line.split()
            direction = parts[0]
            count = int(parts[1])
            self.move(direction, count)

    def num_visited(self, segment: int = -1) -> int:
        return len(self.visited[-1])

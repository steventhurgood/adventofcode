from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Set, Optional, Callable, Generator, List

import re

ProgressFunc = Callable[[Iterable[int], int], Generator]


@dataclass(order=True)
class Range:
    """Range represents an inclusive range of integers"""
    left: int
    right: int
    empty: bool = False

    def __contains__(self, number: int) -> bool:
        if self.empty:
            return False

        return number >= self.left and number <= self.right

    def __len__(self) -> int:
        if self.empty:
            return 0

        return self.right - self.left + 1


@dataclass
class Ranges:
    ranges: List[Range] = field(default_factory=list)

    def add(self, range: Range):
        # todo - keep a sorted list of the left and right bits of
        # each range, so I can merge them by walking and counting.
        if range.empty:
            return

        if len(self.ranges) == 0:
            self.ranges.append(range)
            return

        merged_range: Optional[Range] = None
        range_already_covered: bool = False

        # otherwise merge
        for existing_range in self.ranges:
            # [ existing ][ range ]
            # [ existing [ ] range ]
            if (range.left <= existing_range.right+1
                and
                    range.right > existing_range.right):
                existing_range.right = range.right
                merged_range = existing_range

            # [ range ][ existing ]
            # [ range [ ] existing ]
            if (range.right >= existing_range.left-1
                and
                    range.left < existing_range.left):
                existing_range.left = range.left
                merged_range = existing_range

            #   [ existing [ range ] existing ]
            if (range.left >= existing_range.left
                and
                    range.right <= existing_range.right):
                range_already_covered = True

        # at this point, our newly-merged range may be mergeable again.
        if merged_range is not None:
            # if not, then this is a noop
            self.add(merged_range)
        else:
            if not range_already_covered:
                # our new range does not touch any existing range
                self.ranges.append(range)


@dataclass(frozen=True)
class Vector:
    x: int
    y: int

    def tuning_frequency(self, multiplier: int = 4000000):
        return self.x * multiplier + self.y


@dataclass(frozen=True)
class Sensor:
    position: Vector
    beacon: Vector

    max_distance: int

    @classmethod
    def create(cls, position: Vector, beacon: Vector) -> Sensor:
        x_offset = abs(position.x - beacon.x)
        y_offset = abs(position.y - beacon.y)

        max_distance = x_offset + y_offset

        return Sensor(
            position,
            beacon,
            max_distance)

    def range_at_row(self, row: int,
                     min_x: Optional[int] = None,
                     max_x: Optional[int] = None) -> Range:
        distance_from_sensor_row = abs(row - self.position.y)
        if distance_from_sensor_row > self.max_distance:
            return Range(0, 0, True)

        extents = abs(self.max_distance-distance_from_sensor_row)
        range_start = self.position.x - extents
        if min_x is not None:
            range_start = max(range_start, min_x)
        range_end = self.position.x + extents
        if max_x is not None:
            range_end = min(range_end, max_x)
        return Range(range_start, range_end)


line_regexp2 = ('Sensor at x=(?P<sensor_x>-?[0-9]+)'
                ', y=(?P<sensor_y>-?[0-9]+)'
                ': closest beacon is at x=(?P<beacon_x>-[0-9]+)'
                ', (?P<beacon_y>-?[0-9]+)=15')

line_regexp = ('Sensor at x=(?P<sensor_x>-?[0-9]+)'
               ', y=(?P<sensor_y>-?[0-9]+)'
               ': closest beacon is at x=(?P<beacon_x>-?[0-9]+)'
               ', y=(?P<beacon_y>-?[0-9]+)')


class Sensors:
    sensors: Set[Sensor]
    beacons: Set[Vector]

    def __init__(self, filename: str):
        line_re = re.compile(line_regexp)
        self.sensors = set()
        self.beacons = set()

        with open(filename) as f:
            for line in f:
                m = line_re.match(line.strip())
                if m is None:
                    raise Exception(
                        f'line "{line}" did not match "{line_regexp}"')
                position = Vector(
                    x=int(m.group('sensor_x')),
                    y=int(m.group('sensor_y')),
                )
                beacon = Vector(
                    x=int(m.group('beacon_x')),
                    y=int(m.group('beacon_y'))
                )
                self.sensors.add(Sensor.create(position, beacon))
                self.beacons.add(beacon)

    def ranges_at_row(self, y: int,
                      min_x: Optional[int] = None,
                      max_x: Optional[int] = None,
                      include_beacons: bool = False) -> Ranges:
        ranges = Ranges()
        for sensor in self.sensors:
            range = sensor.range_at_row(y, min_x, max_x)
            ranges.add(range)
        return ranges

    def find_beacon_for_row(self, y: int, max_x: int, potential_xs: Set[int]) -> Optional[Vector]:
        covered_xs = self.x_that_cannot_contain_a_beacon(
            y, 0, max_x, include_beacons=True)
        candidates: Set[int] = potential_xs - covered_xs
        if len(candidates) > 1:
            raise Exception('Error: there should only be one valid '
                            'solution. Found: {candidates} at y={y}')
        if len(candidates) == 1:
            x = candidates.pop()
            return Vector(x, y)
        return None

    def find_beacon(self, max_x: int, max_y: int,
                    progress: Optional[ProgressFunc] = None) -> Vector:
        potential_xs = set(range(max_x+1))
        if progress is not None:
            with progress(range(max_y), length=max_y) as rows:
                for y in rows:
                    v = self.find_beacon_for_row(y, max_x, potential_xs)
                    if v is not None:
                        return v
        else:
            for y in range(max_y):
                v = self.find_beacon_for_row(y, max_x, potential_xs)
                if v is not None:
                    return v

        raise Exception('No valid beacons found')

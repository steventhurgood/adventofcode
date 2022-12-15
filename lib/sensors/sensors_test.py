
import unittest
import os
from lib.sensors import Sensors, Vector, Ranges, Range

from dataclasses import dataclass

from typing import List, Tuple

default_filename = os.path.join(os.path.dirname(
    __file__), 'test_data', 'test_data.txt')


@dataclass
class RangeTestCase:
    description: str
    ranges: List[Tuple[int, int]]
    want: List[Tuple[int, int]]


class TestSensors(unittest.TestCase):

    def test_coverage(self):
        sensors = Sensors(default_filename)
        x = sensors.ranges_at_row(10)
        self.assertEqual(len(x), 26)

    def test_find_beacon(self):
        sensors = Sensors(default_filename)
        beacon = sensors.find_beacon(20, 20)

        self.assertEqual(beacon, Vector(14, 11))
        self.assertEqual(beacon.tuning_frequency(), 56000011)

    def test_ranges(self):
        tests: List[RangeTestCase] = [
            RangeTestCase(
                description='no overlapping range',
                ranges=[(1, 10), (20, 30)],
                want=[(1, 10), (20, 30)]
            ),
            RangeTestCase(
                description='touching left',
                ranges=[(1, 10), (11, 20)],
                want=[(1, 20)]
            ),
            RangeTestCase(
                description='touching right',
                ranges=[(11, 20), (1, 10)],
                want=[(1, 20)]
            ),
            RangeTestCase(
                description='contained',
                ranges=[(1, 20), (5, 15)],
                want=[(1, 20)]
            ),
            RangeTestCase(
                description='containing',
                ranges=[(5, 15), (1, 20)],
                want=[(1, 20)]
            ),
            RangeTestCase(
                description='merge left',
                ranges=[(1, 15), (5, 20)],
                want=[(1, 20)]
            ),
            RangeTestCase(
                description='merge right',
                ranges=[(5, 20), (1, 15)],
                want=[(1, 20)]
            ),
            RangeTestCase(
                description='merge recursive',
                ranges=[(1, 5), (15, 20), (5, 15)],
                want=[(1, 20)]
            ),
            RangeTestCase(
                description='singletons',
                ranges=[(1, 1), (2, 2)],
                want=[(1, 2)]
            )
        ]
        for test in tests:
            ranges = Ranges()
            for range in test.ranges:
                ranges.add(Range(range[0], range[1]))
            got = []
            for range in ranges.ranges:
                got.append((range.left, range.right))
            self.assertSetEqual(set(got), set(test.want),
                                f'Error adding ranges for {test.description}')

    def test_contains(self):
        test_range = Range(1, 10)
        singleton_range = Range(1, 1)
        empty_range = Range(0, 0, True)
        self.assertTrue(1 in test_range)
        self.assertTrue(10 in test_range)
        self.assertFalse(11 in test_range)
        self.assertTrue(1 in singleton_range)
        self.assertFalse(0 in empty_range)

    def test_range_len(self):
        test_range = Range(1, 10)
        singleton_range = Range(1, 1)
        empty_range = Range(0, 0, True)

        self.assertEqual(len(test_range), 10)
        self.assertEqual(len(singleton_range), 1)
        self.assertEqual(len(empty_range), 0)

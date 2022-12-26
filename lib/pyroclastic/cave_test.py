import itertools
import os
import unittest

from lib.pyroclastic import Wind, Rock, Rocks, Position, Cave

from typing import Sequence

default_filename = os.path.join(os.path.dirname(
    __file__), 'test_data', 'test_data.txt')


class TestCave(unittest.TestCase):
    def test_wind(self):
        wind = Wind('<<><')

        got = list(itertools.islice(wind, 0, 10))
        want = '<<><<<><<<'

        self.assertSequenceEqual(got, want)

    def test_rocks(self):
        rocks = Rocks()

        rock_1 = set([
            Position(0, 0), Position(1, 0), Position(2, 0), Position(3, 0)
        ])

        rock_2 = set([
            Position(1, 2),
            Position(0, 1), Position(1, 1), Position(2, 1),
            Position(1, 0),
        ])

        rock_3 = set([
            Position(2, 2),
            Position(2, 1),
            Position(0, 0), Position(1, 0), Position(2, 0),
        ])

        rock_4 = set([
            Position(0, 3),
            Position(0, 2),
            Position(0, 1),
            Position(0, 0),
        ])

        rock_5 = set([
            Position(0, 1), Position(1, 1),
            Position(0, 0), Position(1, 0),
        ])

        want_rocks: Sequence[Rock] = list(map(Rock, [
            rock_1,
            rock_2,
            rock_3,
            rock_4,
            rock_5,
            rock_1,
            rock_2,
            rock_3,
            rock_4,
            rock_5,
        ]))

        got_rocks = list(itertools.islice(rocks, 0, 10))

        self.assertSequenceEqual(got_rocks, want_rocks)

    def test_drop(self):
        cave = Cave(default_filename)

        cave.drop_rock()
        self.assertEqual(cave.max_y + cave.collapsed, 1)

    def test_drops(self):
        cave = Cave(default_filename)

        cave.drop_rocks(2022)
        self.assertEqual(cave.max_y + cave.collapsed, 3068)

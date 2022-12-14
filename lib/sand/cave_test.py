import unittest
from lib.sand import CaveBuilder
import os

import textwrap

test_filename = os.path.join(os.path.dirname(
    __file__), 'test_data', 'test_data.txt')


class CaveTest(unittest.TestCase):

    def test_build(self):
        cave = CaveBuilder(test_filename).build()
        want = textwrap.dedent('''\
                                  ..........
                                  ..........
                                  ..........
                                  ..........
                                  ....#...##
                                  ....#...#.
                                  ..###...#.
                                  ........#.
                                  ........#.
                                  #########.''')

        got = str(cave)
        self.assertEqual(got, want)

    def test_simulate(self):
        cave = CaveBuilder(test_filename).build()

        while cave.simulate():
            pass

        self.assertEqual(cave.cycle_count, 24)

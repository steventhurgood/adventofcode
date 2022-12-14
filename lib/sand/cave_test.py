import unittest
from lib.sand import CaveBuilder
import os

import textwrap
import logging

test_filename = os.path.join(os.path.dirname(
    __file__), 'test_data', 'test_data.txt')

logging.basicConfig()
logger = logging.getLogger(__name__)


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

        while cave.simulate(max_cycles=100):
            strcave = str(cave)
            logger.info(strcave)
            pass

        self.assertEqual(cave.cycle_count, 24)

    def test_simulate_with_floor(self):
        cave = CaveBuilder(test_filename).build(has_floor=True)

        while cave.simulate(max_cycles=100):
            strcave = str(cave)
            logger.info(strcave)
            pass

        self.assertEqual(cave.cycle_count, 93)

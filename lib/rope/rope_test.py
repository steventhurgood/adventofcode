import unittest

import os

from typing import TextIO
from absl import logging


from lib.rope.rope import Rope


class TestRope(unittest.TestCase):
    test_input: TextIO

    def setUp(self) -> None:
        logging.set_stderrthreshold('info')
        test_filename1 = os.path.join(
            os.path.dirname(__file__), 'test_data/test_data.txt')
        test_filename2 = os.path.join(
            os.path.dirname(__file__), 'test_data/test_data2.txt')

        self.test_input = open(test_filename1)
        self.test_input2 = open(test_filename2)
        return super().setUp()

    def test_moves(self):
        want = 13
        rope = Rope()
        rope.process(self.test_input)
        got = rope.num_visited()

        self.assertEqual(got, want)

    def test_longrope(self):
        want = 1
        rope = Rope(10)
        rope.process(self.test_input)
        got = rope.num_visited(9)
        self.assertEqual(got, want)

    def test_longrope2(self):
        want = 36
        rope = Rope(10)
        rope.process(self.test_input2)
        got = rope.num_visited(9)
        self.assertEqual(got, want)

    def tearDown(self) -> None:
        self.test_input.close()
        self.test_input2.close()
        return super().tearDown()

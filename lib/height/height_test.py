import unittest
import os

from lib.height import Heights

test_filename = os.path.join(os.path.dirname(
    __file__), 'test_data', 'test_data.txt')


class TestHeights(unittest.TestCase):

    def test_path_finder(self):
        with open(test_filename) as f:
            heights = Heights(f)
        heights.find_path()

        self.assertEqual(heights.steps, 31)

    def test_shortest_path_to_a(self):
        with open(test_filename) as f:
            heights = Heights(f)
        heights.find_shortest_path_to_a()

        self.assertEqual(heights.steps, 29)

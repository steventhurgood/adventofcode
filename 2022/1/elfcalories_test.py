import os
import unittest

from .elfcalories import ElfCalories

test_data_filename = os.path.join(
    os.path.dirname(__file__), 'data/test_data.txt')


class TestElfCaloriesMax(unittest.TestCase):
    testdata: str

    def setUp(self) -> None:
        with open(test_data_filename) as f:
            self.testdata = f.read()
        return super().setUp()

    def test_most_calories(self):
        elfCalories = ElfCalories(self.testdata)
        self.assertEqual(elfCalories.largest_total_calories(), 24000)

    def test_most_calories3(self):
        elfCalories = ElfCalories(self.testdata)
        self.assertEqual(elfCalories.largest_total_calories(3), 45000)

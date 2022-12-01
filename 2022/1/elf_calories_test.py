import os
import unittest

from elf_calories import ElfCalories

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
        self.assertEqual(elfCalories.largest(), 24000)

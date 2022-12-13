"""Comparable tests"""

import os
import unittest
from dataclasses import dataclass
from typing import Any, List

from lib.compare import Comparable

test_filename = os.path.join(os.path.dirname(
    __file__), 'test_data', 'test_data.txt')


@dataclass
class ComparisonTestCase:
    """Test case for the Comparable class"""
    first: List[Any]
    second: List[Any]
    right_order: bool


class TestCompare(unittest.TestCase):
    """Unit tests for compare"""

    def test_comparisons(self):
        """Test comparisons for Comparable objects"""
        tests = [
            ComparisonTestCase(
                [1],
                [1],
                False
            ),
            ComparisonTestCase(
                [1, 1, 3, 1, 1],
                [1, 1, 5, 1, 1],
                True
            ),
            ComparisonTestCase(
                [[1], [2, 3, 4]],
                [[1], 4],
                True
            ),
            ComparisonTestCase(
                [9],
                [[8, 7, 6]],
                False
            ),
            ComparisonTestCase(
                [[4, 4], 4, 4],
                [[4, 4], 4, 4, 4],
                True
            ),
            ComparisonTestCase(
                [7, 7, 7, 7],
                [7, 7, 7],
                False,
            ),
            ComparisonTestCase(
                [],
                [3],
                True,
            ),
            ComparisonTestCase(
                [[[]]],
                [[]],
                False
            ),
            ComparisonTestCase(
                [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
                [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
                False
            )
        ]

        for test in tests:
            first = Comparable.build_comparable(test.first)
            second = Comparable.build_comparable(test.second)

            if test.right_order:
                self.assertLess(
                    first, second, f'Error comparing {first} < {second}')
            else:
                self.assertLessEqual(
                    second, first, f'Error comparing {second} <= {first}')

    def test_parsing(self):
        """Test that parsing a pairs file is successful"""
        pairs, _ = Comparable.compile_comparable_pairs(test_filename)

        sum_indexes = 0
        for i, (left, right) in enumerate(pairs):
            if left < right:
                # indexes start at 1
                sum_indexes += (i+1)

        self.assertEqual(sum_indexes, 13)

    def test_decoder_key(self):
        """Test that calculating the decoder key words"""

        _, compiler = Comparable.compile_comparable_pairs(test_filename)
        decoder_key = compiler.find_decoder_key()
        self.assertEqual(decoder_key, 140)

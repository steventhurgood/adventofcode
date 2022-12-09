import unittest
import os

from lib.trees.tree import Trees

test_filename = os.path.join(os.path.dirname(
    __file__), 'test_data/test_data.txt')


class TreeTest(unittest.TestCase):
    treeData: Trees

    def setUp(self):
        self.treeData = Trees()
        with open(test_filename) as f:
            self.treeData.process(f)

    def test_visible(self):
        visible = self.treeData.count_visible()
        self.assertEqual(visible, 21)

    def test_scenic_score(self):
        want_scores = [
            [0, 0, 0, 0, 0],
            [0, 1, 4, 1, 0],
            [0, 6, 1, 2, 0],
            [0, 1, 8, 3, 0],
            [0, 0, 0, 0, 0],
        ]
        for y, row in enumerate(want_scores):
            for x, want_score in enumerate(row):
                score = self.treeData.scenic_score(x, y)
                self.assertEqual(
                    score, want_score, f'Scores did not match {score} != {want_score} at ({x}, {y})')

    def test_best_score(self):
        score, best_x, best_y = self.treeData.best_scenic_score()
        self.assertEqual(
            score, 8, f'Scores did not match at ({best_x}, {best_y})')

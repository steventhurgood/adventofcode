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

    def test_best_score(self):
        score = self.treeData.best_scenic_score()
        self.assertEqual(score, 8)

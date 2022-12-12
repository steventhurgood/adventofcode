
from lib.monkey import Monkeys

import unittest
import os

test_filename = os.path.join(os.path.dirname(
    __file__), 'test_data', 'test_data.txt')


class TestMonkey(unittest.TestCase):

    def test_one_round(self):
        monkeys = Monkeys(test_filename)

        tests = [

            [  # after one round
                [20, 23, 27, 26],
                [2080, 25, 167, 207, 401, 1046],
                [],
                [],
            ],
            [  # after two rounds
                [695, 10, 71, 135, 350],
                [43, 49, 58, 55, 362],
                [],
                [],
            ]
        ]

        for monkeys_want in tests:
            monkeys.round()
            for i, want in enumerate(monkeys_want):
                self.assertEqual(monkeys.monkeys[i].items, want)

    def test_monkey_business(self):
        monkeys = Monkeys(test_filename)
        monkeys.round(20)
        wants = [101, 95, 7, 105]
        for i, want in enumerate(wants):
            self.assertEqual(monkeys.monkeys[i].inspection_count, want)

        got = monkeys.monkey_business()
        self.assertEqual(got, 10605)

    def test_worrier(self):
        monkeys = Monkeys(test_filename, worrier=True)
        tests = [
            {
                'rounds': 1,
                'want': [2, 4, 3, 6]
             },{
                'rounds': 20-1, # after 20 rounds total
                'want': [99, 97, 8, 103]
             },{
                'rounds': 1000-20, # after 1000 rounds total
                'want': [5204, 4792, 199, 5192]
             },{
                'rounds': 2000-1000, # after 2000 rounds total
                'want': [10419, 9577, 392, 10391]
             },{
                'rounds': 3000-2000,
                'want': [15638, 14358, 587, 15593]
             },{
                'rounds': 10000-3000,
                'want': [52166, 47830, 1938, 52013]
             }
        ]
        for test in tests:
            monkeys.round(test['rounds'])
            got = monkeys.inspection_counts()
            self.assertEqual(got, test['want'])

        got = monkeys.monkey_business()
        self.assertEqual(got, 2713310158)

    
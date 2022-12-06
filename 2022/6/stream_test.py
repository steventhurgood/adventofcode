import unittest

import lib.stream


class TestStream(unittest.TestCase):
    def test_find_offset(self):
        tests = [
            ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4, 7),
            ('bvwbjplbgvbhsrlpgdmjqwftvncz', 4, 5),
            ('nppdvjthqldpwncqszvftbrmjlhg', 4, 6),
            ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4, 10),
            ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4, 11),
            ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14, 19),
            ('bvwbjplbgvbhsrlpgdmjqwftvncz', 14, 23),
            ('nppdvjthqldpwncqszvftbrmjlhg', 14, 23),
            ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14, 29),
            ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14, 26)
        ]

        for test in tests:
            want = test[2]
            got = lib.stream.find_offset(test[0], test[1])
            self.assertEqual(
                got, want,  f'find_offset({test[0]}, {test[1]}) != {test[2]}')

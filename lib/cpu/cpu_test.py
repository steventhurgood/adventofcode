import unittest

import os

from lib.cpu.cpu import CPU

test_filename1 = os.path.join(os.path.dirname(
    __file__), 'test_data', 'test_data.txt')
test_filename2 = os.path.join(os.path.dirname(
    __file__), 'test_data', 'test_data2.txt')


class TestCPU(unittest.TestCase):

    def test_cpu(self):
        cpu: CPU = CPU()
        cpu.execute(test_filename1)

        cycles_want = [
            1,  # initial value
            1,  # after noop
            1,  # addx has started but not finished
            4,  # addx 3 has finished
        ]

        for cycle, want in enumerate(cycles_want):
            got = cpu.register_after(cycle)
            self.assertEqual(
                got, want, f'Unexpected value of register after {cycle} cycles: {got} != {want} ')

    def test_cpu2(self):
        cpu: CPU = CPU()
        cpu.execute(test_filename2)

        cycles_want = [
            (19, 21),  # during the 20th cycle
            (59, 19),  # during the 60th cycle
            (99, 18),  # during the 100th cycle
            (139, 21),  # during the 140th cycle
            (179, 16),  # during the 180th cycle
            (219, 18)  # during the 220th cycle
        ]

        for cycle, want in cycles_want:
            got = cpu.register_after(cycle)
            self.assertEqual(
                got, want, f'Unexpected value of register after {cycle} cycles: {got} != {want} ')

    def test_cpu_strengths(self):
        cpu = CPU()
        cpu.execute(test_filename2)

        strengths = cpu.strengths([20, 60, 100, 140, 180, 220])
        self.assertEqual(sum(strengths), 13140)

    def test_render(self):
        cpu = CPU()
        cpu.execute(test_filename2)
        got = cpu.render()
        want = '\n'.join([
            '##..##..##..##..##..##..##..##..##..##..',
            '###...###...###...###...###...###...###.',
            '####....####....####....####....####....',
            '#####.....#####.....#####.....#####.....',
            '######......######......######......####',
            '#######.......#######.......#######.....',
        ])
        self.assertEqual(got, want)

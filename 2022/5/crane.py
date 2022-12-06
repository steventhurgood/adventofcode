from typing import Sequence, List

from absl import app, logging

import os

default_filename = os.path.join(
    os.path.dirname(__file__), 'data/data.txt')


class Crane:
    stacks: List[List[str]]

    def __init__(self):
        self.stacks = []

    def process(self, input: Sequence[str]):
        state_lines = []
        for line in input:
            if line == '\n':
                break  # end of initial instructions
            state_lines.append(line)

        stack_numbers = [int(n) for n in state_lines[-1].split()]
        for s in stack_numbers:
            self.stacks.append([])
        # line length is 3 * the number of stacks + (stacks-1) for the spaces
        # eg., for 3 stacks, 11 chars (+ '\n')
        # [Z] [M] [P]
        # stack values at i=1, 5, 9 (every 4 chars)
        for state in state_lines[:-1]:  # don't include the last line
            for stack in range(len(self.stacks)):
                offset = (stack) * 4 + 1
                value = state[offset]
                if value != ' ':
                    self.stacks[stack].insert(0, value)

        logging.info(f'initial state: {self.stacks}')
        for line in input:
            # move 1 from 2 to 1
            line = line.strip()
            logging.info(f'instruction: {line}')
            parts = line.split()
            count = int(parts[1])
            from_stack = int(parts[3])
            to_stack = int(parts[5])
            self.multimove(count, from_stack, to_stack)

        logging.info(f'final state: {self.stacks}')

    def move(self, count: int, from_stack: int, to_stack: int):
        for i in range(count):
            # stacks are 0 indexed, but instructions start at 1
            value = self.stacks[from_stack-1].pop()
            self.stacks[to_stack-1].append(value)

    def multimove(self, count: int, from_stack: int, to_stack: int):
        values = self.stacks[from_stack-1][-count:]
        self.stacks[from_stack-1] = self.stacks[from_stack-1][:-count]

        # stacks are 0 indexed, but instructions start at 1
        self.stacks[to_stack-1].extend(values)

    def topcrates(self) -> str:
        return ''.join([stack[-1] for stack in self.stacks])


def main(argv):
    c = Crane()
    with open(default_filename) as f:
        c.process(f)
    print(c.topcrates())


if __name__ == '__main__':
    app.run(main)

#!/usr/bin/env python3

from absl import app, flags

from elfcalories import ElfCalories
import sys

FLAGS = flags.FLAGS

flags.DEFINE_string('input', '', 'input filename')
flags.DEFINE_integer('n', 1, 'number of largest elves')


def main(argv):
    with open(FLAGS.input) as f:
        data = f.read()
        elfCalories = ElfCalories(data)
        largest = elfCalories.largest_total_calories(FLAGS.n)
        print(largest)


if __name__ == '__main__':
    app.run(main)

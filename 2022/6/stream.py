
import os

import lib.stream

from absl import app, flags

FLAGS = flags.FLAGS
test_filename = os.path.join(os.path.dirname(__file__), 'data/data.txt')

flags.DEFINE_integer('n', 4, 'number of unique chars')
flags.DEFINE_string('input', test_filename, 'input filename')


def main(argv):
    with open(FLAGS.input) as f:
        for line in f:
            offset = lib.stream.find_offset(line.strip(), FLAGS.n)
            if len(line) > 80:
                line = line[:77] + '...'
            print(f'({offset}) {line}')


if __name__ == '__main__':
    app.run(main)

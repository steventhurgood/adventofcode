from absl import app, flags
import os

from lib.rope.rope import Rope

default_filename = os.path.join(os.path.dirname(__file__), 'data/data.txt')

FLAGS = flags.FLAGS

flags.DEFINE_string('input', default_filename, 'input file')
flags.DEFINE_integer('length', 10, 'rope length')


def main(argv):
    rope = Rope(FLAGS.length)
    with open(FLAGS.input) as f:
        rope.process(f)
        print(rope.num_visited())


if __name__ == '__main__':
    app.run(main)

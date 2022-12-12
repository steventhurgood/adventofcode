import os

from absl import app, flags

from lib.monkey import Monkeys

default_filename = os.path.join(os.path.dirname(__file__), 'data', 'data.txt')

FLAGS = flags.FLAGS
flags.DEFINE_string('input', default_filename, 'default filename')
flags.DEFINE_integer('rounds', 1000, 'number of rounds')
flags.DEFINE_bool('worrier', True,
                  'reduce worry by a third each round if false')


def main(argv):
    monkeys = Monkeys(FLAGS.input, FLAGS.worrier)
    monkeys.round(FLAGS.rounds)
    print(monkeys.monkey_business())


if __name__ == '__main__':
    app.run(main)

import os
from absl import app, flags, logging

from lib.height import Heights

default_filename = os.path.join(os.path.dirname(__file__), 'data', 'data.txt')

FLAGS = flags.FLAGS
flags.DEFINE_string('input', default_filename, 'input filename')


def main(argv):
    with open(FLAGS.input) as f:
        heights = Heights(f)
        print(heights)
    heights.find_shortest_path_to_a()
    print(heights)
    print(f'Steps taken: {heights.steps}')


if __name__ == '__main__':
    app.run(main)

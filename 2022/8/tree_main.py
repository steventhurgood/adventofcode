from absl import app, flags
from lib.trees.tree import Trees

import os

default_input = os.path.join(os.path.dirname(__file__), 'data/data.txt')

flags.DEFINE_string('input', default_input, 'input filename')
FLAGS = flags.FLAGS


def main(argv):
    trees = Trees()
    with open(FLAGS.input) as f:
        trees.process(f)
        visible = trees.count_visible()
        print(f'{visible} trees are visible')

        best_score, x, y = trees.best_scenic_score()
        print(f'Best score {best_score} found at ({x}, {y})')


if __name__ == '__main__':
    app.run(main)

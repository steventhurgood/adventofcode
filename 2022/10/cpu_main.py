import os

from lib.cpu import CPU

from absl import app, logging, flags

default_filename = os.path.join(os.path.dirname(__file__), 'data', 'data.txt')

FLAGS = flags.FLAGS
flags.DEFINE_string('input', default_filename, 'input filename')
flags.DEFINE_list('cycles', [20, 60, 100, 140, 180, 220],
                  'cycles at which to calculate the strength')


def main(argv):
    cpu = CPU()
    cpu.execute(FLAGS.input)
    strengths = cpu.strengths(FLAGS.cycles)
    logging.info(f'Strengths: {strengths}')
    print(f'Total strength: {sum(strengths)}')

    output = cpu.render()
    print(output)


if __name__ == '__main__':
    app.run(main)

import os

import apache_beam as beam
import apache_beam.io.fileio as fileio
from absl import app, flags
from apache_beam.options.pipeline_options import PipelineOptions
import elfcalories.beamlib as eb
FLAGS = flags.FLAGS

default_input = '2022/1/data/test_data.txt'

flags.DEFINE_string('input', default_input,
                    'File containing elf calorie data')

flags.DEFINE_integer('n', 3, 'Number of top calorific elves')


def main(argv):
    print('Hello')
    print(os.getcwd())
    beam_options = PipelineOptions(
        runner='DirectRunner',
    )

    with beam.Pipeline(options=beam_options) as p:
        _ = (
            p
            | 'Find Files' >> fileio.MatchFiles(FLAGS.input)
            | 'Read Matches' >> fileio.ReadMatches()
            | 'Process Files' >> beam.ParDo(eb.FileReaderFn())
            | eb.LargestElves(FLAGS.n)
            | 'Print Results' >> beam.Map(print)
        )


if __name__ == '__main__':
    app.run(main)

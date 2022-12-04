import apache_beam as beam
import apache_beam.io.fileio as fileio


class FileReaderFn(beam.DoFn):
    def process(self, element: fileio.ReadableFile):
        d: bytes = element.read()
        yield d


class RecordSplitterFn(beam.DoFn):
    def process(self, element: bytes):
        for i, record in enumerate(element.split(b'\n\n')):
            yield (i, record)


class RecordProcessorFn(beam.DoFn):
    def process(self, element):
        k, v = element
        for n in v.split(b'\n'):
            yield (k, int(n))


@beam.ptransform_fn
def LargestElves(pcoll: beam.PCollection, n: int) -> beam.PCollection:
    return (
        pcoll
        | 'Read Files' >> beam.ParDo(RecordSplitterFn())
        | 'Process Records' >> beam.ParDo(RecordProcessorFn())
        | 'Sum Calories' >> beam.CombinePerKey(sum)
        | 'Get Values' >> beam.Values()
        | 'Find Top N' >> beam.combiners.Top.Largest(n)
        | 'Global Sum' >> beam.Map(sum)
    )

import lib.elfcalories.beamlib as eb
from apache_beam.testing.util import equal_to
from apache_beam.testing.util import assert_that
from apache_beam.testing.test_pipeline import TestPipeline
import apache_beam as beam
import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


test_data_filename = os.path.join(
    os.path.dirname(__file__), 'data/test_data.txt')


class TestElfCaloriesMax(unittest.TestCase):
    testdata: str

    def setUp(self):
        self.testdata = open(test_data_filename).read()

    def test_elfcalories_one(self):
        with TestPipeline() as p:
            input = p | beam.Create(
                [bytes(self.testdata, 'utf-8')])

            output = input | 'Assert' >> eb.LargestElves(
                1)
            assert_that(output, equal_to([24000]))

    def test_elfcalories_three(self):
        with TestPipeline() as p:
            input = p | beam.Create(
                [bytes(self.testdata, 'utf-8')])

            output: beam.PCollection = input | 'Assert Three' >> eb.LargestElves(
                3)
            assert_that(output, equal_to([45000]))

import os

import click

from lib.compare import Comparable

default_filename = os.path.join(os.path.dirname(__file__), 'data', 'data.txt')


@click.command()
@click.option('--input', type=click.Path(exists=True), default=default_filename)
@click.option('--verbose', type=bool, default=False)
def compare(input, verbose):
    """compare is the main function of compare_main

    It reads in a file containing pairs of comparable lists,
    and returns how many of them were correctly sorted.

    Args:
        input_filename (str): filename containing pairs of lists
    """
    pairs, compiler = Comparable.compile_comparable_pairs(input)
    sum_indexes = 0
    sum_ordered = 0
    for i, (left, right) in enumerate(pairs):
        if left < right:
            # indexes start at 1
            sum_ordered += 1
            sum_indexes += (i+1)

    click.echo(
        f'({sum_ordered}/{len(pairs)}({sum_indexes}) pairs are in the correct order')

    decoder_key = compiler.find_decoder_key()

    if verbose:
        for comparable in compiler.comparables:
            click.echo(comparable)

    click.echo(
        f'The decoder key is {decoder_key} ([{compiler.key_a_index}, {compiler.key_b_index}]')


if __name__ == '__main__':
    compare()


import os
from lib.sand import CaveBuilder, Cave

import click

default_filename = os.path.join(os.path.dirname(__file__), 'data', 'data.txt')


@click.command()
@click.option('--input', type=click.Path(), default=default_filename)
@click.option('--verbose', type=bool, default=False)
@click.option('--print_every', type=int, default=1)
@click.option('--has_floor', type=bool, default=True)
def simulate_cave(input: str, verbose: bool, print_every: int, has_floor: bool):
    cave: Cave = CaveBuilder(input).build(has_floor)

    while cave.simulate():
        if verbose:
            if cave.cycle_count % print_every == 0:
                click.echo(str(cave))

    click.echo(f'Simulation terminated after {cave.cycle_count} cycles')


if __name__ == '__main__':
    simulate_cave()

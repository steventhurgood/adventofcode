
import click
import os

from lib.pyroclastic import Cave

default_filename = os.path.join(os.path.dirname(__file__), 'data', 'data.txt')


@click.command()
@click.option('--input', default=default_filename, type=click.Path())
# @click.option('--num_rocks', '-n', default=2022, type=int)
@click.option('--num_rocks', '-n', default=1000000000000, type=int)
def cave_fall(input: click.Path, num_rocks: int):
    cave = Cave(input)
    cave.drop_rocks(num_rocks, click.progressbar)

    click.echo(f'highest rock is {cave.max_y + cave.collapsed}')


if __name__ == '__main__':
    cave_fall()

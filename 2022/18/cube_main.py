import click
from lib.cubes import Cubes

import os

default_filename = os.path.join(os.path.dirname(__file__), 'data', 'data.txt')


@click.command()
@click.option('--input', default=default_filename, type=click.Path())
@click.option('--holes', type=bool, default=True)
def main(input: str, holes: bool):
    cubes = Cubes.from_file(input)
    surface_area = cubes.surface_area(test_for_holes=holes)
    holes_description = ''
    if holes:
        holes_description = ' excluding sealed holes'
    click.echo(
        f'Surface area of {len(cubes)} cubes = {surface_area}{holes_description}')


if __name__ == '__main__':
    main()

import os
import time

import click

from lib.sensors import Sensors

default_filename = os.path.join(os.path.dirname(__file__), 'data', 'data.txt')


@click.command()
@click.option('--input', type=click.Path(), default=default_filename)
@click.option('--row', type=int, default=2000000)
@click.option('--max', type=int, default=4000000)
def sensors(input: click.Path, row: int, max: int):
    s = Sensors(input)
    start_time = time.time()
    result = s.x_that_cannot_contain_a_beacon(row)
    end_time = time.time()
    duration = end_time - start_time
    click.echo(
        f'{len(result)} locations at row {row} cannot contain a beacon'
        f' ({duration} seconds)')

    beacon = s.find_beacon(max_x=max, max_y=max, progress=click.progressbar)
    tuning_frequency = beacon.tuning_frequency()
    click.echo(
        f'Beacon {beacon} found with tuning frequency: {tuning_frequency}')


if __name__ == '__main__':
    sensors()

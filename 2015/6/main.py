
import os

from typing import List

data_file = os.path.join(os.path.dirname(__file__), "data/data.txt")


class LightGrid:
    lights: List[List[bool]]

    def __init__(self, width: int = 1000, height: int = 1000):
        self.lights = []
        for y in range(height):
            self.lights.append([0]*width)

    def range_coords(self, from_xy: str, to_xy: str):
        from_x, from_y = [int(n) for n in from_xy.split(',')]
        to_x, to_y = [int(n) for n in to_xy.split(',')]

        for x in range(from_x, to_x+1):
            for y in range(from_y, to_y+1):
                yield (x, y)

    def on(self, from_xy: str, to_xy: str):
        for x, y in self.range_coords(from_xy, to_xy):
            self.lights[y][x] += 1

    def off(self, from_xy: str, to_xy: str):
        for x, y in self.range_coords(from_xy, to_xy):
            self.lights[y][x] -= 1
            if self.lights[y][x] < 0:
                self.lights[y][x] = 0

    def toggle(self, from_xy: str, to_xy: str):
        for x, y in self.range_coords(from_xy, to_xy):
            self.lights[y][x] += 2

    def count(self) -> int:
        total = 0
        for row in self.lights:
            total += sum(row)
        return total

    def process(self, input):
        for line in input:
            parts = line.split(' ')
            if line.startswith('turn off'):
                self.off(parts[2], parts[4])
            if line.startswith('turn on'):
                self.on(parts[2], parts[4])
            if line.startswith('toggle'):
                self.toggle(parts[1], parts[3])


lg = LightGrid()

with open(data_file) as f:
    lg.process(f)
    print(lg.count())

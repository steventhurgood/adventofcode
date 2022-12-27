import os
import unittest

from lib.cubes import Cube, Cubes, Face, Position

default_filename = os.path.join(os.path.dirname(
    __file__), 'test_data', 'test_data.txt')


class CubeTest(unittest.TestCase):

    def test_get_faces(self):

        cube = Cube(Position(3, 4, 5))

        want = {
            Face.from_vertices([  # front with z=5
                Position(3, 4, 5),
                Position(3, 5, 5),
                Position(4, 5, 5),
                Position(4, 4, 5),
            ],
                Position(0, 0, -1),
            ),
            Face.from_vertices([  # back with z=6
                Position(3, 4, 6),
                Position(3, 5, 6),
                Position(4, 5, 6),
                Position(4, 4, 6),
            ],
                Position(0, 0, 1),
            ),
            Face.from_vertices([  # bottom with y=4
                Position(3, 4, 5),
                Position(3, 4, 6),
                Position(4, 4, 6),
                Position(4, 4, 5),
            ],
                Position(0, -1, 0),
            ),
            Face.from_vertices([  # top with y=5
                Position(3, 5, 5),
                Position(3, 5, 6),
                Position(4, 5, 6),
                Position(4, 5, 5),
            ],
                Position(0, 1, 0),
            ),
            Face.from_vertices([  # left with x=3
                Position(3, 4, 5),
                Position(3, 5, 5),
                Position(3, 5, 6),
                Position(3, 4, 6),
            ],
                Position(-1, 0, 0),
            ),
            Face.from_vertices([  # right with x=4
                Position(4, 4, 5),
                Position(4, 5, 5),
                Position(4, 5, 6),
                Position(4, 4, 6)
            ],
                Position(1, 0, 0),
            ),
        }

        got = cube.faces()

        self.assertEqual(got, want)

    def test_simple_surface_area(self):
        test_cubes = [
            (Position(1, 1, 1), Position(0, 1, 1)),  # left
            (Position(1, 1, 1), Position(2, 1, 1)),  # right

            (Position(1, 1, 1), Position(1, 0, 1)),  # below
            (Position(1, 1, 1), Position(1, 2, 1)),  # above

            (Position(1, 1, 1), Position(1, 1, 0)),  # in front
            (Position(1, 1, 1), Position(1, 1, 2)),  # behind
        ]
        for test in test_cubes:
            cubes: Cubes = Cubes(
                cubes=set(map(Cube, test))
            )
            surface_area = cubes.surface_area()
            self.assertEqual(
                surface_area, 10, f'surface area failed for {test}')

    def test_surface_area(self):
        cubes = Cubes.from_file(default_filename)
        got = cubes.surface_area()
        want = 64
        self.assertEqual(got, want)

    def test_holes(self):
        cubes = Cubes.from_file(default_filename)

        self.assertNotIn(Position(2, 2, 5), cubes.external_positions)

        for x in range(cubes.min_position.x, cubes.max_position.x+1):
            for y in range(cubes.min_position.y, cubes.max_position.y+1):
                for z in range(cubes.min_position.z, cubes.max_position.z+1):
                    position = Position(x, y, z)
                    if position == Position(2, 2, 5):  # the only hole
                        continue

                    if Cube(position) in cubes.cubes:
                        self.assertNotIn(position, cubes.external_positions)
                    else:
                        self.assertIn(position, cubes.external_positions)

    def test_surface_area_with_holes(self):
        cubes = Cubes.from_file(default_filename)
        got = cubes.surface_area(test_for_holes=True)
        want = 58
        self.assertEqual(got, want)

    def test_surface_area_differences(self):
        cubes = Cubes.from_file(default_filename)

        for cube in cubes.cubes:
            for face in cube.faces():
                is_external_no_holes = cubes.is_external(cube, face, False)
                is_external_holes = cubes.is_external(cube, face, True)

                # these two should be equal, unless the face is facing 2, 2, 5
                facing = cube.position + face.normal

                if facing == Position(2, 2, 5):
                    continue

                self.assertEqual(is_external_holes,
                                 is_external_no_holes,
                                 f'cube {cube}, face{face.normal} give different results: '
                                 f'{is_external_no_holes=} {is_external_holes=}')

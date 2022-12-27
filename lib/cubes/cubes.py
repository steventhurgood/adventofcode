from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import FrozenSet, Iterable, List, Set, Tuple

logging.basicConfig()
logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Position:
    """Position represents a location in 3-dimensional space.
    """
    x: int
    y: int
    z: int

    def __add__(self, other: Position):
        return Position(self.x + other.x, self.y + other.y, self.z + other.z)

    def adjacent(self,
                 min_position: Position,
                 max_position: Position) -> Set[Position]:
        offsets = [
            Position(-1, 0, 0),
            Position(1, 0, 0),
            Position(0, -1, 0),
            Position(0, 1, 0),
            Position(0, 0, -1),
            Position(0, 0, 1),
        ]
        adjacent_positions = set()

        for offset in offsets:
            offset_position = self + offset
            if (
                offset_position.x < min_position.x
                or
                offset_position.x > max_position.x
                or
                offset_position.y < min_position.y
                or
                offset_position.y > max_position.y
                or
                offset_position.z < min_position.z
                or
                offset_position.z > max_position.z
            ):
                continue
            adjacent_positions.add(offset_position)

        return adjacent_positions


@dataclass(frozen=True)
class Face:
    """Face represents a 1x1 face of a cube.
    vertices are specified in clockwide order facing in the positive
    axis direction.


        A---B
       /   /|   Y
      /   / |   ^  Z
     /   /  |   | /
    C---D   E   |/
    |   |  /    --> X
    |   | /
    |   |/
    F---G

    For now we ignore that and use unordered Positions for a face

    """
    vertices: FrozenSet[Position]
    normal: Position = field(compare=False)

    @classmethod
    def from_vertices(cls, vertices: Iterable[Position], normal: Position):
        return cls(frozenset(vertices), normal)


@dataclass(frozen=True)
class Cube:
    """Cube represents a 1x1x1 cube whose coordinates start at position.

    eg., if Position = 3,4,5 then the cube fills the space:

    x: [3, 4]
    y: [4, 5]
    z: [5, 6]
    """
    position: Position

    def faces(self) -> Set[Face]:
        face_offsets: List[
            Tuple[Position, Position, Position, Position, Position
                  ]] = [
            (   # left at x=0
                Position(0, 0, 0),
                Position(0, 1, 0),
                Position(0, 1, 1),
                Position(0, 0, 1),
                Position(-1, 0, 0),  # facing left
            ),
            (   # right at x=1
                Position(1, 0, 0),
                Position(1, 0, 1),
                Position(1, 1, 1),
                Position(1, 1, 0),
                Position(1, 0, 0),  # facing right
            ),
            (  # bottom at y=0
                Position(0, 0, 0),
                Position(0, 0, 1),
                Position(1, 0, 1),
                Position(1, 0, 0),
                Position(0, -1, 0),  # facing down
            ),
            (  # top at y=1
                Position(0, 1, 0),
                Position(1, 1, 0),
                Position(1, 1, 1),
                Position(0, 1, 1),
                Position(0, 1, 0),  # facing up

            ),
            (  # front at z=0
                Position(0, 0, 0),
                Position(1, 0, 0),
                Position(1, 1, 0),
                Position(0, 1, 0),
                Position(0, 0, -1),  # facing towards
            ),
            (  # back at z=1
                Position(0, 0, 1),
                Position(0, 1, 1),
                Position(1, 1, 1),
                Position(1, 0, 1),
                Position(0, 0, 1),  # facing away
            )
        ]
        faces: Set[Face] = set()
        for face in face_offsets:
            vertices: List[Position] = []
            for vertex_offset in face[:4]:
                vertices.append(self.position + vertex_offset)
            faces.add(Face.from_vertices(vertices, face[4]))

        return faces


@dataclass
class Cubes:
    cubes: Set[Cube]
    min_position: Position = field(init=False)
    max_position: Position = field(init=False)
    external_positions: Set[Position] = field(default_factory=set)

    def __post_init__(self):
        self.set_extents()
        self.find_external()

    def set_extents(self):
        xs = list(map(lambda cube: cube.position.x, self.cubes))
        ys = list(map(lambda cube: cube.position.y, self.cubes))
        zs = list(map(lambda cube: cube.position.z, self.cubes))
        min_x = min(xs)
        min_y = min(ys)
        min_z = min(zs)

        max_x = max(xs)
        max_y = max(ys)
        max_z = max(zs)

        self.min_position = Position(min_x, min_y, min_z)
        self.max_position = Position(max_x, max_y, max_z)

    def find_external(self):
        candidates: Set[Position] = set()

        # fill the candidates with the most extremel positions
        # that are not already in a block.

        # left
        x = self.min_position.x
        for y in range(self.min_position.y, self.max_position.y+1):
            for z in range(self.min_position.z, self.max_position.z+1):
                position = Position(x, y, z)
                if Cube(position) not in self.cubes:
                    candidates.add(position)

        # right
        x = self.max_position.x
        for y in range(self.min_position.y, self.max_position.y+1):
            for z in range(self.min_position.z, self.max_position.z+1):
                position = Position(x, y, z)
                if Cube(position) not in self.cubes:
                    candidates.add(position)
        # bottom
        y = self.min_position.y
        for x in range(self.min_position.x, self.max_position.x+1):
            for z in range(self.min_position.z, self.max_position.z+1):
                position = Position(x, y, z)
                if Cube(position) not in self.cubes:
                    candidates.add(position)
        # top
        y = self.max_position.y
        for x in range(self.min_position.x, self.max_position.x+1):
            for z in range(self.min_position.z, self.max_position.z+1):
                position = Position(x, y, z)
                if Cube(position) not in self.cubes:
                    candidates.add(position)
        # front
        z = self.min_position.z
        for x in range(self.min_position.x, self.max_position.x+1):
            for y in range(self.min_position.y, self.max_position.y+1):
                position = Position(x, y, z)
                if Cube(position) not in self.cubes:
                    candidates.add(position)
        # back
        z = self.max_position.z
        for x in range(self.min_position.x, self.max_position.x+1):
            for y in range(self.min_position.y, self.max_position.y+1):
                position = Position(x, y, z)
                if Cube(position) not in self.cubes:
                    candidates.add(position)

        while len(candidates) > 0:
            candidate = candidates.pop()
            self.external_positions.add(candidate)

            for adjacent_position in candidate.adjacent(
                    self.min_position, self.max_position):
                if Cube(adjacent_position) in self.cubes:
                    # this adjacent cube is already occupied
                    continue

                if adjacent_position in self.external_positions:
                    # we've already determined that this adjacent
                    # cube is external
                    continue

                candidates.add(adjacent_position)

    @classmethod
    def from_file(cls, filename: str):
        cubes: List[Cube] = []

        with open(filename) as f:
            for line in f:
                match line.strip().split(','):
                    case [x, y, z]:
                        cubes.append(Cube(Position(int(x), int(y), int(z))))
                    case _:
                        raise Exception(f'invalid line: {line}')
        return Cubes(set(cubes))

    def __len__(self) -> int:
        return len(self.cubes)

    def surface_area(self, test_for_holes: bool = False) -> int:
        external_face_count: int = 0

        for cube in self.cubes:
            for face in cube.faces():
                if self.is_external(cube, face, test_for_holes):
                    logger.info(
                        f'Face {face.normal} of cube {cube} is external')
                    external_face_count += 1

        return external_face_count

    def is_external(self,
                    cube: Cube,
                    face: Face,
                    test_for_holes: bool = False) -> bool:

        # start with the position next to the face
        position = cube.position + face.normal
        if test_for_holes:
            return (
                self.outside_extents(position)
                or
                position in self.external_positions
            )

        return Cube(position) not in self.cubes

    def outside_extents(self, position: Position) -> bool:
        min_position = self.min_position
        max_position = self.max_position
        return (
            position.x < min_position.x
            or
            position.x > max_position.x
            or
            position.y < min_position.y
            or
            position.y > max_position.y
            or
            position.z < min_position.z
            or
            position.z > max_position.z
        )

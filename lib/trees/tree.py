
import dataclasses
from typing import List, Sequence, Tuple, TextIO

from absl import logging


@dataclasses.dataclass
class Trees:
    trees: List[List[int]] = dataclasses.field(default_factory=list)
    num_rows: int = 0
    num_cols: int = 0

    def process(self, input: TextIO):
        for line in input:
            self.trees.append(list(map(int, line.strip())))

        self.num_rows = len(self.trees)
        if self.num_rows > 0:
            self.num_cols = len(self.trees[0])

    def best_scenic_score(self) -> Tuple[int, int, int]:
        best_score = 0
        best_x = 0
        best_y = 0

        # all edge trees have a best scenic score of 0
        for y in range(1, self.num_rows-1):
            for x in range(1, self.num_cols-1):
                score = self.scenic_score(x, y)
                if score > best_score:
                    logging.info(
                        f'New best score found {score} > {best_score} at [{x}, {y}]')
                    best_score = score
                    best_x = x
                    best_y = y
        return best_score, best_x, best_y

    def scenic_score(self, start_x: int, start_y: int) -> int:

        if (start_x == 0
            or start_x == len(self.trees[0])-1
            or start_y == 0
            or start_y == len(self.trees)-1
            ):
            return 0
        # stop at the first tree that is >= the tree under consideration
        # shorter trees further away are not visible
        # look left
        for x in range(start_x-1, -1, -1):
            if self.trees[start_y][x] >= self.trees[start_y][start_x]:
                #    left_distance = start_x - x
                break
            # if self.trees[start_y][x] >= current_highest_tree:
        left_distance = start_x - x
        #    current_highest_tree = self.trees[start_y][x]

        # look right
        for x in range(start_x+1, self.num_cols):
            if self.trees[start_y][x] >= self.trees[start_y][start_x]:
                # right_distance = x - start_x
                break
            # if self.trees[start_y][x] >= current_highest_tree:
        right_distance = x - start_x
        #        current_highest_tree = self.trees[start_y][x]

        # look up
        for y in range(start_y-1, -1, -1):
            if self.trees[y][start_x] >= self.trees[start_y][start_x]:
               # up_distance = start_y - y
                break
            # if self.trees[y][start_x] >= current_highest_tree:
        up_distance = start_y - y
        #        current_highest_tree = self.trees[y][start_x]

        # look down
        for y in range(start_y+1, self.num_rows):
            if self.trees[y][start_x] >= self.trees[start_y][start_x]:
                # down_distance = y - start_y
                break
            # if self.trees[y][start_x] >= current_highest_tree:
        down_distance = y - start_y
        #        current_highest_tree = self.trees[y][start_x]
        return left_distance * right_distance * up_distance * down_distance

    def count_visible(self) -> int:
        visible: List[List[int]] = []
        for row in self.trees:
            # all trees start as hidden
            visible.append([0] * len(row))
        # outer square is visible:
        for y in range(self.num_rows):
            visible[y][0] = 1
            visible[y][-1] = 1

        for x in range(self.num_cols):
            visible[0][x] = 1
            visible[-1][x] = 1

        # look left
        for y in range(1, self.num_rows-1):
            row = self.trees[y]
            previous_highest_tree = row[0]
            for x in range(1, self.num_cols-1):
                if row[x] > previous_highest_tree:
                    visible[y][x] = 1
                    previous_highest_tree = row[x]

        # look right
        for y in range(1, self.num_rows-1):
            row = self.trees[y]
            previous_highest_tree = row[-1]
            for x in range(self.num_cols-1, 0, -1):
                if row[x] > previous_highest_tree:
                    visible[y][x] = 1
                    previous_highest_tree = row[x]
        # look up
        for x in range(1, self.num_cols-1):
            row = [self.trees[y][x] for y in range(self.num_rows)]
            previous_highest_tree = row[0]
            for y in range(1, self.num_rows-1):
                if row[y] > previous_highest_tree:
                    visible[y][x] = 1
                    previous_highest_tree = row[y]

        # look down
        for x in range(1, self.num_cols-1):
            row = [self.trees[y][x] for y in range(self.num_rows)]
            previous_highest_tree = row[-1]
            for y in range(self.num_rows-1, 0, -1):
                if row[y] > previous_highest_tree:
                    visible[y][x] = 1
                    previous_highest_tree = row[y]

        visible_count = 0
        for row in visible:
            visible_count += sum(row)

        return visible_count

from typing import Optional
from typing import Sequence
from typing import List


class Elf:
    """class Elf represents an elf who is carrying some calories
    """
    calories: List[int]

    def __init__(self):
        self.calories = []

    def add_calories(self, n: int):
        self.calories.append(n)

    def total_calories(self) -> int:
        return sum(self.calories)


class ElfCalories:
    elves: List[Elf] = []

    def __init__(self, input_data: str):
        current_elf: Optional[Elf] = None
        for line in input_data.strip().split('\n'):
            if current_elf is None:
                current_elf = Elf()

            if line == '':
                self.elves.append(current_elf)
                current_elf = None
                continue

            number = int(line)
            current_elf.add_calories(number)
        if current_elf is not None:
            self.elves.append(current_elf)

    def largest(self, n: int = 1) -> Sequence[Elf]:
        sorted_elves = sorted(self.elves, key=lambda e: e.total_calories())
        return sorted_elves[-n:]

    def largest_total_calories(self, n: int = 1) -> int:
        l: Sequence[Elf] = self.largest(n)
        return sum(e.total_calories() for e in l)

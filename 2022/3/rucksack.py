
from collections import defaultdict

from typing import Dict
from typing import List
from typing import Set

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

priorities = {l: p+1 for p, l in enumerate(letters)}
print(priorities)

with open("2022/3/data/data.txt") as f:
    duplicates: List[str] = []
    for line in f:
        compartment_a: Dict[str, int] = defaultdict(int)
        compartment_b: Dict[str, int] = defaultdict(int)

        items = line.strip()
        num_items = len(line)
        for item in items[:num_items // 2]:
            compartment_a[item] += 1
        for item in items[num_items // 2:]:
            compartment_b[item] += 1
            if item in compartment_a:
                duplicates.append(item)
                break
    print(sum([priorities[l] for l in duplicates]))


elves: List[Set[str]] = []

with open("2022/3/data/data.txt") as f:
    for line in f:
        elves.append(set(line.strip()))

print(elves)

badges: List[str] = []

for group in range(0, len(elves), 3):
    elf_a = elves[group]
    elf_b = elves[group+1]
    elf_c = elves[group+2]

    common: str = elf_a.intersection(elf_b).intersection(elf_c).pop()
    badges.append(common)

print(badges)
print([priorities[b] for b in badges])
print(sum([priorities[b] for b in badges]))

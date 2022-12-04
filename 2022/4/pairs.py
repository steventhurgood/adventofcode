
import os

input_filename = os.path.join(os.path.dirname(__file__), "data/data.txt")

duplicates = 0
overlaps = 0

with open(input_filename) as f:
    for line in f:
        # 2-4,6-8
        range_a, range_b = line.strip().split(',')
        range_a_start, range_a_end = [int(n) for n in range_a.split('-')]
        range_b_start, range_b_end = [int(n) for n in range_b.split('-')]

        if ((range_a_start <= range_b_start and range_a_end >= range_b_end) or (range_b_start <= range_a_start and range_b_end >= range_a_end)):
            duplicates += 1

        if (
            (range_a_start >= range_b_start and range_a_start <= range_b_end)
            or
            (range_a_end >= range_b_start and range_a_end <= range_b_end)
            or
            (range_b_start >= range_a_start and range_b_start <= range_a_end)
            or
            (range_b_end >= range_a_start and range_b_end <= range_a_end)
        ):
            overlaps += 1

print(duplicates)
print(overlaps)

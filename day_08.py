#!/usr/bin/env python3

import pprint
import itertools

matrix = []
with open("input/08/test_input", "r") as file:
    # with open("input/08/real_input", "r") as file:
    for line in file:
        matrix.append(list(line.strip()))

frequencies = set()
for rank in matrix:
    for cell in rank:
        frequencies.add(cell)

frequencies.remove(".")

print(f"frequencies: {len(frequencies)}")

frequency_locations = {}
for frequency in frequencies:
    frequency_locations[frequency] = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == frequency:
                print(f"frequency: {frequency} found at {i}, {j}")
                frequency_locations[frequency].append((i, j))

pprint.pprint(frequency_locations)

antinodes = set()

for frequency in frequency_locations:
    print(f"frequency: {frequency}")
    print(f"frequency_locations: {frequency_locations[frequency]}")
    antenna_pairs = list(itertools.combinations(frequency_locations[frequency], 2))
    print(f"antenna_pairs: {antenna_pairs}")

    for antenna_pair in antenna_pairs:
        delta_x = antenna_pair[0][0] - antenna_pair[1][0]
        delta_y = antenna_pair[0][1] - antenna_pair[1][1]

        antinode_a = (antenna_pair[0][0] + delta_x, antenna_pair[0][1] + delta_y)
        antinode_b = (antenna_pair[1][0] - delta_x, antenna_pair[1][1] - delta_y)

        print("antenna_pair: ", antenna_pair)

        print(f"antinode_a: {antinode_a}")
        print(f"antinode_b: {antinode_b}")

        antinodes.add(antinode_a)
        antinodes.add(antinode_b)

antinode_locations = 0
for antinode in antinodes:
    print(f"antinode: {antinode}")
    if (antinode[0] >= 0 and antinode[0] < len(matrix)) and (
        antinode[1] >= 0 and antinode[1] < len(matrix[0])
    ):
        print(f"antinode: {antinode} is in matrix")
        antinode_locations += 1

print(f"antinode_locations: {antinode_locations}")

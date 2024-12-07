#!/usr/bin/env python3

import pprint

matrix = []
# with open("input/06/test_input", "r") as file:
with open("input/06/real_input", "r") as file:
    for line in file:
        matrix.append(list(line.strip()))

# pprint.pprint(matrix)
open_spaces = []
blocked_spaces = []
cursor = (None, None)
heading = 0  # degrees
visited_spaces = set()

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if matrix[i][j] == ".":
            open_spaces.append((i, j))
        elif matrix[i][j] == "#":
            blocked_spaces.append((i, j))
        elif matrix[i][j] == "^":
            guard = (i, j)

print(f"Guard at {guard}")
while (
    guard[0] >= 0
    and guard[0] < len(matrix)
    and guard[1] >= 0
    and guard[1] < len(matrix[0])
):  # is still on the board?
    visited_spaces.add(guard)
    if heading == 0:
        # up
        next_space = (guard[0] - 1, guard[1])
    elif heading == 90:
        # right
        next_space = (guard[0], guard[1] + 1)
    elif heading == 180:
        # down
        next_space = (guard[0] + 1, guard[1])
    elif heading == 270:
        # left
        next_space = (guard[0], guard[1] - 1)
    if next_space in blocked_spaces:
        heading = (heading + 90) % 360
    else:
        guard = next_space

print(f"Visited spaces: {len(visited_spaces)}")

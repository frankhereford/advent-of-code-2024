#!/usr/bin/env python3

import pprint
import time

matrix = []
with open("input/06/test_input", "r") as file:
    # with open("input/06/real_input", "r") as file:
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
            initial_guard_location = (i, j)
            matrix[i][j] = "."

iterations = 0


def draw_board(matrix, space, guard, heading):
    if heading == 0:
        guard_symbol = "↑"
    elif heading == 90:
        guard_symbol = "→"
    elif heading == 180:
        guard_symbol = "↓"
    elif heading == 270:
        guard_symbol = "←"
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if (i, j) == space:
                print("S", end="")
            elif (i, j) == guard:
                print(guard_symbol, end="")
            else:
                print(matrix[i][j], end="")
        print()


loop_found = 0
for space in open_spaces:
    print(f"Trying {space}.")
    # reset the board
    guard = initial_guard_location
    heading = 0
    visited_spaces = set()
    iterations = 0

    while (
        guard[0] >= 0
        and guard[0] < len(matrix)
        and guard[1] >= 0
        and guard[1] < len(matrix[0])
    ):  # is still on the board?
        # print(f"Guard at {guard} for iteration {iterations}.")
        iterations += 1
        if iterations > 10000:
            loop_found += 1
            break

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
        if next_space in blocked_spaces or next_space == space:
            heading = (heading + 90) % 360
        else:
            guard = next_space
        # draw_board(matrix, space, guard, heading)
        # time.sleep(0.2)
        # input()

    print(f"Visited {len(visited_spaces)} spaces in {iterations} iterations.")

print(
    f"Visited spaces: {len(visited_spaces)} in {iterations} iterations with {loop_found} loop spots."
)

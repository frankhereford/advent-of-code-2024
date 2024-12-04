#!/usr/bin/env python3

import pprint

matrix = []
# with open("input/04/test_input_part_1", "r") as file:
with open("input/04/real_input", "r") as file:
    for line in file:
        matrix.append(list(line.strip()))

xmas = ["X", "M", "A", "S"]

pprint.pprint(matrix)

find_count = 0

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        # print()

        is_right = True
        try:
            for x in range(0, len(xmas)):
                # print(f"Checking ({i}, {j + x}) {matrix[i][j + x]} == {xmas[x]}")
                if not matrix[i][j + x] == xmas[x]:
                    is_right = False
                    break
        except IndexError:
            is_right = False

        is_down_right = True
        try:
            for x in range(0, len(xmas)):
                # print(
                #     f"Checking ({i + x}, {j + x}) {matrix[i + x][j + x]} == {xmas[x]}"
                # )
                if not matrix[i + x][j + x] == xmas[x]:
                    is_down_right = False
                    break

        except IndexError:
            is_down_right = False

        is_down = True
        try:
            for x in range(0, len(xmas)):
                # print(f"Checking ({i + x}, {j}) {matrix[i + x][j]} == {xmas[x]}")
                if not matrix[i + x][j] == xmas[x]:
                    is_down = False
                    break
        except IndexError:
            is_down = False

        is_down_left = True
        try:
            for x in range(0, len(xmas)):
                if j - x < 0:
                    is_down_left = False
                    break
                # print(
                #     f"Checking ({i + x}, {j - x}) {matrix[i + x][j - x]} == {xmas[x]}"
                # )
                if not matrix[i + x][j - x] == xmas[x]:
                    is_down_left = False
                    break

        except IndexError:
            is_down_left = False

        is_left = True
        try:
            for x in range(0, len(xmas)):
                if j - x < 0:
                    is_left = False
                    break
                # print(f"Checking ({i}, {j - x}) {matrix[i][j - x]} == {xmas[x]}")
                if not matrix[i][j - x] == xmas[x]:
                    is_left = False
                    break
        except IndexError:
            is_left = False

        is_up_left = True
        try:
            for x in range(0, len(xmas)):
                if i - x < 0 or j - x < 0:
                    is_up_left = False
                    break
                # print(
                #     f"Checking ({i - x}, {j - x}) {matrix[i - x][j - x]} == {xmas[x]}"
                # )
                if not matrix[i - x][j - x] == xmas[x]:
                    is_up_left = False
                    break
        except IndexError:
            is_up_left = False

        is_up = True
        try:
            for x in range(0, len(xmas)):
                if i - x < 0:
                    is_up = False
                    break
                # print(f"Checking ({i - x}, {j}) {matrix[i - x][j]} == {xmas[x]}")
                if not matrix[i - x][j] == xmas[x]:
                    is_up = False
                    break
        except IndexError:
            is_up = False

        is_up_right = True
        try:
            for x in range(0, len(xmas)):
                if i - x < 0:
                    is_up_right = False
                    break
                # print(
                #     f"Checking ({i - x}, {j + x}) {matrix[i - x][j + x]} == {xmas[x]}"
                # )
                if not matrix[i - x][j + x] == xmas[x]:
                    is_up_right = False
                    break
        except IndexError:
            is_up_right = False

        if is_right:
            print(f"Found right XMAS starting at ({i}, {j})")
            find_count += 1
        if is_down_right:
            print(f"Found down-right XMAS starting at ({i}, {j})")
            find_count += 1
        if is_down:
            print(f"Found down XMAS starting at ({i}, {j})")
            find_count += 1
        if is_down_left:
            print(f"Found down-left XMAS starting at ({i}, {j})")
            find_count += 1
        if is_left:
            print(f"Found left XMAS starting at ({i}, {j})")
            find_count += 1
        if is_up_left:
            print(f"Found up-left XMAS starting at ({i}, {j})")
            find_count += 1
        if is_up:
            print(f"Found up XMAS starting at ({i}, {j})")
            find_count += 1
        if is_up_right:
            print(f"Found up-right XMAS starting at ({i}, {j})")
            find_count += 1

print(f"Found {find_count} XMASs ✅")


print("\n\n\n\n")


found_count = 0
for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[i]) - 1):
        # print(f"\nChecking {i}, {j}")

        # gotta have an A at the center of the X
        if not matrix[i][j] == "A":
            print(f"{i}, {j}: No A")
            continue

        # gotta have the right set of letters around the A
        if not {
            matrix[i - 1][j - 1],
            matrix[i - 1][j + 1],
            matrix[i + 1][j - 1],
            matrix[i + 1][j + 1],
        } == set(["M", "M", "S", "S"]):
            print(f"{i}, {j}: Wrong letters")
            continue

        # make sure we have MAS's, not MAM's or SAS's
        if (
            matrix[i - 1][j - 1] == matrix[i + 1][j + 1]
            or matrix[i + 1][j - 1] == matrix[i - 1][j + 1]
        ):
            print(f"{i}, {j}: MAM and/or SAS")
            continue

        print(f"bingo!, A at {i}, {j}")
        found_count += 1

print(f"Found {found_count} XMASs ✅")

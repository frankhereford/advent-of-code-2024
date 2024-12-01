#!/usr/bin/env python3
import re

pattern = re.compile(r"(\d+)\s+(\d+)")
first_set = []
second_set = []

with open("input/01/test_input", "r") as file:
    for line in file:
        match = pattern.search(line.strip())
        if match:
            first_set.append(int(match.group(1)))
            second_set.append(int(match.group(2)))

first_set.sort()
second_set.sort()
total_distance = 0

for i in range(len(first_set)):
    distance = abs(first_set[i] - second_set[i])
    total_distance += distance
    print(f"{i}: {first_set[i]} {second_set[i]} → {distance}")

print(f"Total distance: {total_distance}")

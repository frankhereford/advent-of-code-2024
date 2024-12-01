#!/usr/bin/env python3

import re

# two integers separated by whitespace
pattern = re.compile(r"(\d+)\s+(\d+)")

first_set = []
second_set = []

# parse file and populate the lists
with open("input/01/real_input", "r") as file:
    for line in file:
        match = pattern.search(line.strip())
        if match:
            first_set.append(int(match.group(1)))
            second_set.append(int(match.group(2)))

# sort them as instructed
first_set.sort()
second_set.sort()

# accumulator for final answer
total_distance = 0

# we assume the lists are the same length
for i in range(len(first_set)):
    distance = abs(first_set[i] - second_set[i])
    total_distance += distance
    print(f"{i}: {first_set[i]} {second_set[i]} → {distance}")

print(f"Total distance: {total_distance} ✅")

# hash to store frequency of values in the second set
second_set_hash = {}

# accumulator for final answer
total_similarity_score = 0

# count the occurrences of each number in the second list
for number in second_set:
    second_set_hash[number] = second_set_hash.get(number, 0) + 1

# iterate over the first list and calculate the similarity score
for number in first_set:
    if number in second_set_hash:
        similarity_score = number * second_set_hash[number]
        total_similarity_score += similarity_score
        print(f"Found {number} in second set, score of {similarity_score}")

print(f"Total similarity score: {total_similarity_score} ✅")

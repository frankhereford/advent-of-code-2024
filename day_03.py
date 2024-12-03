#!/usr/bin/env python3

import re

multiplication_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

sum_of_products = 0
with open("input/03/test_input", "r") as file:
    safe_count = 0
    for line in file:
        # print(line)
        matches = multiplication_pattern.finditer(line.strip())
        for match in matches:
            # print(match)
            sum_of_products += int(match.group(1)) * int(match.group(2))

# print(f"Sum of products: {sum_of_products} ✅")

# zwa_multiplication_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

remove_nonexecutable_lines = re.compile(r"(^|do\(\))(.*?)(don't\(\)|$)")

sum_of_products = 0
with open("input/03/part_b_test_input", "r") as file:
    safe_count = 0
    for line in file:
        print(line)
        matches = remove_nonexecutable_lines.finditer(line.strip())
        for match in matches:
            # print("new iteration:")
            # print(match)
            # print(match.group(1))
            # print(match.group(2))
            # print(match.group(3))
            inner_matches = multiplication_pattern.finditer(match.group(2))
            for inner_match in inner_matches:
                print(inner_match)
                sum_of_products += int(inner_match.group(1)) * int(inner_match.group(2))

print(f"Sum of products: {sum_of_products} ✅")

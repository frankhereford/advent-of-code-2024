#!/usr/bin/env python3

import re

multiplication_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

sum_of_products = 0
with open("input/03/real_input", "r") as file:
    safe_count = 0
    for line in file:
        # print(line)
        matches = multiplication_pattern.finditer(line.strip())
        for match in matches:
            # print(match)
            sum_of_products += int(match.group(1)) * int(match.group(2))

print(f"Sum of products: {sum_of_products} ✅")

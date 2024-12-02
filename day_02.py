#!/usr/bin/env python3


def is_gradually_changing(levels):
    for i in range(1, len(levels)):
        change = abs(int(levels[i]) - int(levels[i - 1]))
        if not change >= 1 or not change <= 3:
            return False
    return True


with open("input/02/test_input", "r") as file:
    safe_count = 0
    for line in file:
        levels = line.split()
        sorted_levels = sorted(levels)
        reverse_sorted_levels = sorted(levels, reverse=True)
        if levels == sorted_levels or levels == reverse_sorted_levels:
            if is_gradually_changing(levels):
                safe_count += 1

print(f"Safe count: {safe_count}")

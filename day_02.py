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
        print()
        levels_as_strings = line.split()
        levels = list(map(int, levels_as_strings))

        possible_dampened_levels = []
        for i in range(0, len(levels)):
            possible_dampened_levels.append(levels[:i] + levels[i + 1 :])

        print(f"Levels: {levels}")
        for dampened_levels in possible_dampened_levels:
            print(f"Dampened levels: {dampened_levels}")
            sorted_levels = sorted(dampened_levels)
            reverse_sorted_levels = sorted(dampened_levels, reverse=True)
            if (
                dampened_levels == sorted_levels
                or dampened_levels == reverse_sorted_levels
            ):
                if is_gradually_changing(dampened_levels):
                    safe_count += 1
                    print(f"{dampened_levels} is safe")
                    break


print(f"Safe count: {safe_count}")

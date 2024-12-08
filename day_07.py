#!/usr/bin/env python3

import itertools
import pprint

sum_of_valid_results = 0

sum_of_valid_results = 0

with open("input/07/test_input", "r") as file:
    # with open("input/07/real_input", "r") as file:
    for line in file:
        print()
        # print(line)
        target_result, equation = line.strip().split(":")
        target_result = int(target_result)
        terms = [int(term) for term in equation.strip().split(" ")]
        print(f"Target Result: {target_result}, terms: {terms}")
        num_operations = len(terms) - 1
        possible_operators = ["+", "*"]
        operator_combinations = list(
            itertools.product(possible_operators, repeat=num_operations)
        )

        print(f"Terms: {terms}")
        print(f"Combinations: {operator_combinations}")

        for operators in operator_combinations:
            first_operand = terms[0]
            for i in range(0, len(operators)):
                if operators[i] == "+":
                    first_operand += terms[i + 1]
                elif operators[i] == "*":
                    first_operand *= terms[i + 1]
            print(f"Result: {first_operand}")
            if first_operand == target_result:
                sum_of_valid_results += target_result
                break

print(f"Sum of valid results: {sum_of_valid_results}")

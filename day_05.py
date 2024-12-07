#!/usr/bin/env python3

import re
import pprint

rule_pattern = re.compile(r"(\d+)\|(\d+)")

rule_pairs = []
updates = []


def is_compliant(update, rule_pair):
    try:
        before_index = update.index(rule_pair[0])
        after_index = update.index(rule_pair[1])
        if before_index < after_index:
            return True
        return False
    except:
        # print("Non-applicable rule")
        return True


with open("input/05/test_input_1", "r") as file:
    # with open("input/05/real_input", "r") as file:
    input_rules = True
    for line in file:
        if line.strip():
            if input_rules:
                # print(line)
                match = rule_pattern.search(line.strip())
                page_before = int(match.group(1))
                page_after = int(match.group(2))
                # print(f"Page {page_before} comes before page {page_after}.")
                rule_pairs.append((page_before, page_after))

            else:  # updates
                updated_pages = [int(x) for x in line.strip().split(",")]
                # print(f"Updated pages: {updated_pages}")
                updates.append(updated_pages)
        else:
            input_rules = False


pprint.pprint(rule_pairs)
pprint.pprint(updates)

sum_of_middles = 0
sum_of_corrected_middles = 0
for update in updates:
    update_ok = True
    for rule in rule_pairs:
        # print(f"Is compliant: {update}, {rule}, {is_compliant(update, rule)}")
        if not is_compliant(update, rule):
            update_ok = False
            break
    print(f"Update {update} compliance status: {update_ok}")
    if update_ok:
        middle_index = int((len(update) - 1) / 2)
        # print(f"Middle index: {middle_index}")
        # print(f"Middle page: {update[middle_index]}")
        sum_of_middles += update[middle_index]
    else:
        did_comply = False
        while not did_comply:
            did_comply = True
            for rule in rule_pairs:
                if rule[0] in update and rule[1] in update:
                    rule_first_element_index = update.index(rule[0])
                    rule_second_element_index = update.index(rule[1])
                    if rule_first_element_index < rule_second_element_index:
                        print(f"{rule} applies and ✅")
                    else:
                        print(f"{rule} applies and ❌")
                        did_comply = False
                        print(f"Before: {update}")
                        previous_value = update[rule_first_element_index]
                        update[rule_first_element_index] = update[
                            rule_second_element_index
                        ]
                        update[rule_second_element_index] = previous_value
                        print(f"After: {update}")

        middle_index = int((len(update) - 1) / 2)
        # print(f"Middle index: {middle_index}")
        # print(f"Middle page: {update[middle_index]}")
        sum_of_corrected_middles += update[middle_index]
print(f"Sum of previously correct middle pages (part 1): {sum_of_middles}")

print(f"Sum of corrected middle pages (part 2): {sum_of_corrected_middles}")

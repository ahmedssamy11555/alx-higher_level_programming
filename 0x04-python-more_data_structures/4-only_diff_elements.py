#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    repeated_element = set()
    diff_elements = set()
    for first_element in set_1:
        for second_element in set_2:
            if first_element == second_element:
                repeated_element.add(first_element)

    for element in set_1.union(set_2):
        if element not in repeated_element:
            diff_elements.add(element)

    return diff_elements

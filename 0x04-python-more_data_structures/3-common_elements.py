#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = set()
    for first_set_element in set_1:
        for second_set_element in set_2:
            if first_set_element == second_set_element:
                common_set.add(first_set_element)
    return common_set

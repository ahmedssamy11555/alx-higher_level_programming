#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in my_list:
        if i < 0 or i > len(my_list) - 1:
            return my_list
        elif i == idx:
            my_list[i] = element
    return my_list

#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    left_pointer = 0
    right_pointer = len(my_list) - 1

    while left_pointer < right_pointer:
        temp = my_list[left_pointer]
        my_list[left_pointer] = my_list[right_pointer]
        my_list[right_pointer] = temp

        left_pointer += 1
        right_pointer -= 1

    return my_list

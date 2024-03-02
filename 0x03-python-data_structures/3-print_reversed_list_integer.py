#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_cpy = my_list[:]
    left_pointer = 0
    right_pointer = len(list_cpy) - 1

    while left_pointer < right_pointer:
        temp = list_cpy[left_pointer]
        list_cpy[left_pointer] = list_cpy[right_pointer]
        list_cpy[right_pointer] = temp

        left_pointer += 1
        right_pointer -= 1
    for number in list_cpy:
        print("{:d}".format(number))

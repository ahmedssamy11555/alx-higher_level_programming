#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list[:]
    if idx < 0 or idx > len(list_copy) - 1:
        return list_copy
    list_copy[idx] = element
    return list_copy
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
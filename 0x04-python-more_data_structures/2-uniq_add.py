#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    uniq_set = set()
    result = 0

    for num in my_list:
        if num not in uniq_set:
            result += num
            uniq_set.add(num)
    return result

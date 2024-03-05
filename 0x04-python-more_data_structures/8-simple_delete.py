#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if not key or key not in a_dictionary:
        return a_dictionary
    for old_key in a_dictionary:
        if old_key == key:
            del a_dictionary[key]
    return a_dictionary

#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    updated_dict = a_dictionary.copy()
    for old_key, old_value in updated_dict.items():
        if old_key == key:
            updated_dict.update({key: value})
    return updated_dict

#!/usr/bin/python3
import hidden_4


def print_module_names():

    module_names = dir(hidden_4)

    for name in sorted(module_names):
        if not name.startswith('__'):
            print(name)


if __name__ == "__main__":
    print_module_names()

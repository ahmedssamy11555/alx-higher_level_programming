#!/usr/bin/python3
import sys


def print_arguments():
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("0 arguments.")
        return

    plural = "" if num_args == 1 else "s"
    print("argument{}: {}.".format(plural, num_args))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")


if __name__ == "__main__":
    print_arguments()

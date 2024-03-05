#!/usr/bin/python3
import sys


def print_arguments():
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("Number of argument(s): 0.")
        return

    plural = "" if num_args == 1 else "s"
    print(f"Number of argument{plural}: {num_args}.")

    print("Arguments:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")


if __name__ == "__main__":
    print_arguments()

#!/usr/bin/python3
import sys


def sum_arguments():
    arguments = sys.argv[1:]
    numbers = [int(arg) for arg in arguments]

    result = sum(numbers)

    print(result)


if __name__ == "__main__":
    sum_arguments()

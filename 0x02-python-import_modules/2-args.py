#!/usr/bin/python3
import sys


def main():
    def print_args(argu):
        print("{} {}:".format(args_length, argu))
        for i, arg in enumerate(args_list):
            if i == 0:
                continue
            print("{}:".format(i), end=" ")
            print("{}".format(arg))

    args_list = sys.argv
    args_length = len(args_list)
    if args_length < 2:
        args_length = 0
        print("{} arguments.".format(args_length))
    elif args_length > 0:
        args_length -= 1

        if args_length == 1:
            print_args("argumnent")
        else:
            print_args("argumnents")


if __name__ == "__main__":
    main()

#!/usr/bin/python3
import sys


def print_args(argu, args_list, args_length):
    print("{} {}:".format(args_length, argu))
    for i, arg in enumerate(args_list):
        print("{}:".format(i+1), end=" ")
        print("{}".format(arg))


def main():
    args_list = sys.argv
    args_length = len(args_list)
    if args_length  == 0:
        print("{} arguments.".format(args_length))
    elif args_length > 0:
        if args_length == 1:
            print_args("argumnent", args_list, args_length)
        else:
            print_args("argumnents", args_list, args_length)


if __name__ == "__main__":
    main()

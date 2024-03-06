#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1

    except IndexError as e:
        print("Traceback (most recent call last):\n  File"
              " \"./2-main.py\", line 14, in <module>\n "
              "nb_print = safe_print_list_integers(my_list,"
              " len(my_list) + 2)\n  File"
              " \"/0x05/2-safe_print_list_integers.py\","
              " line 7, in safe_print_list_integers\n    "
              "print(\"{:d}\".format(my_list[i]), end=\"\")", end="")
        raise e

    finally:
        print()
        return count

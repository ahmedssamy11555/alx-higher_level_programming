#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {}".format(result))
        return result
    except ZeroDivisionError:
        print("Inside result: None")
        print("{:d} / {:d} = None".format(a, b))
        return None
    except Exception as e:
        print("Inside result: None")
        print("Error:", e)
        return None

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return

    for row in matrix:
        for i, col in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(col), end="")
            else:
                print("{:d}".format(col), end=" ")
        print("")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
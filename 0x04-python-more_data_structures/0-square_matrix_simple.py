#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return []

    doubled_matrix = []
    for row in matrix:
        squared_row = []
        for col in row:
            squared_row.append(col ** 2)
        doubled_matrix.append(squared_row)
    return doubled_matrix

#!/usr/bin/python3
"""
Return a new matrix Divided by div value
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    """
    s = "matrix must be a matrix (list of lists) of integers/floats"
    if not (matrix or isinstance(matrix, list)):
        raise TypeError(s)
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if (len(row) == 0):
            raise TypeError(s)
        if (len(row) != len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")
        if not (row or isinstance(row, list)):
            raise TypeError(s)
        for col in row:
            if not (isinstance(col, int) or isinstance(col, float)):
                raise TypeError(s)
    new_matrix = [[round((col / div), 2) for col in row] for row in matrix]
    return (new_matrix)

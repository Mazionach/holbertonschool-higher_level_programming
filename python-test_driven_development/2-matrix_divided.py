#!/usr/bin/python3

""" Division module

This module divides a matrix
"""


def matrix_divided(matrix, div):
    """ Divide each element of matrix by div
    """

    errType = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(errType)
    for r in matrix:
        if not isinstance(r, list) or \
                not all(isinstance(i, (int, float)) for i in r):
            raise TypeError(errType)
    if not all(len(r) == len(matrix[0]) for r in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = matrix.copy()

    for r in range(len(matrix)):
        for i in range(len(matrix[0])):
            new[r][i] = round(new[r][i] / div, 2)

    return new

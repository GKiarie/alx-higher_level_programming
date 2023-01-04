#!/usr/bin/python3
"""
"2-matrix_divided.py" module.
"
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    Arguments:
    matrix: elements can either be ints or floats
    div: must be an int, non zero
    Return: matrix, rounded off to 2dp
    """

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if not isinstance(i, list) or len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(j / div, 2) for j in i] for i in matrix]

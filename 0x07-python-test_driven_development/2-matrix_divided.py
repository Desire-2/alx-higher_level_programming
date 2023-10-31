#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def validate_matrix(matrix):
    """Validates the matrix structure and element types."""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_lengths = [len(row) for row in matrix]
    if not all(length == row_lengths[0] for length in row_lengths):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")


def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div"""
    validate_matrix(matrix)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]

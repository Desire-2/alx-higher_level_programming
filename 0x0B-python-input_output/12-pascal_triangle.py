#!/usr/bin/python3
"""
Module for pascal_triangle method.
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
        Args:
            n (int): number of lists and digits
        Returns: list of lists
    """
    rows = [[1 for j in range(r + 1)] for r in range(n)]
    for n in range(n):
        for r in range(n - 1):
            rows[n][r + 1] = sum(rows[n - 1][r:r + 2])
    return rows

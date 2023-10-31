#!/usr/bin/python3
"""
This is the "4-print_square" module.
The 4-print_square module supplies one function, print_square(size).
"""


def print_square(size):
    """Prints a square with '#'s of length 'size' on each side."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        square_row = '#' * size + '\n'
        square = square_row * size
        print(square, end="")


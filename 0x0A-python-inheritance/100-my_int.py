#!/usr/bin/python3
"""Defines a class MyInt that inherits from int
and reverses the behavior of '!=' and '==' operators."""

class MyInt(int):
    """Class inheriting from int
    but reverses the behavior of '!=' and '==' operators."""

    def __eq__(self, other):
        """Override the '==' operator to perform inequality."""

        return super().__ne__(other)

    def __ne__(self, other):
        """Override the '!=' operator to perform equality."""

        return super().__eq__(other)


#!/usr/bin/python3
"""
This module defines a Rectangle Object.
"""
class Rectangle:
    """Rectangle object with getters and setters for width and height
    """
    def __init__(self, width=0, height=0):
        self._height = height
        self._width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._validate_dimension(value, "width")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._validate_dimension(value, "height")
        self._height = value

    def _validate_dimension(self, value, attribute):
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")


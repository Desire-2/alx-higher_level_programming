#!/usr/bin/python3
"""Module base_geometry
Creates a class
"""


class BaseGeometry:
    """Class with public instance method"""

    def area(self):
        """Raises a NotImplementedError with the message
        'area() is not implemented'
        """

        raise Exception('area() is not implemented')

#!/usr/bin/python3
"""Module inherits_from
Finds if the object is an instance of a class that inherited
(directly/indirectly) from the specified class"""


def inherits_from(obj, base_class):
    """Determines if obj is an instance of a class that
    inherited from base_class

    Args:
        - obj: object to inspect
        - base_class: class to evaluate

    Returns: True if obj is an instance of a class
    inherited from base_class, False otherwise
    """

    return isinstance(obj, base_class) and type(obj) != base_class

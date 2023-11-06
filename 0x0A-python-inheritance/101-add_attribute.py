#!/usr/bin/python3
"""Defines a function to check and add an attribute to an object."""

def add_attribute(obj, attr_name, attr_value):
    """
    Checks if an attribute attr_name with value attr_value can be added to obj.

    Args:
    - obj: Object to add the attribute to
    - attr_name: Name of the attribute
    - attr_value: Value of the attribute to add
    """

    # Checking if an attribute can be added
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("Cannot add a new attribute")
    if hasattr(obj, '__slots__') and not hasattr(obj, attr_name):
        raise TypeError("Cannot add a new attribute")

    # Set the attribute to the object
    setattr(obj, attr_name, attr_value)

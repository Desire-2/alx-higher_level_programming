#!/usr/bin/python3
"""Module: Object_Attribute_Lookup
    Retrieves a collection of available
    attributes and methods associated with an object.
"""

def lookup(obj):
    """Obtains a list containing the attributes and
    methods of the specified object.

    Args:
        - obj: The object whose attributes and
        methods are to be examined.
    """

    return dir(obj)

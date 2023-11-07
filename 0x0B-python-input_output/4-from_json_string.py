#!/usr/bin/python3
"""
from_json_string module
"""
import json

def from_json_string(json_string):
    """
    Converts a JSON string into a Python object.
    Args:
        json_string (str): A JSON string to convert into a Python object.
    Returns:
        object: Python object representing the JSON string.
    """
    return json.loads(json_string)

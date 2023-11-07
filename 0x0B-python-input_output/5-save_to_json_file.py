#!/usr/bin/python3
"""
save_to_json module
"""
import json

def save_to_json_file(obj, filename):
    """
    save_to_json_file - writes an object to a text
    file using JSON representation
    Args:
        obj: The object to be written
        filename: The name of the file
    """
    with open(filename, "w") as file:
        json.dump(obj, file)

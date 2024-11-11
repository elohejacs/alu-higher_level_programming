#!/usr/bin/python3
"""Task 3"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    Args:
        my_obj (any): The object to be serialized.
    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)

#!/usr/bin/python3
"""Task 4"""


import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure)
    Args:
        my_str (str): The JSON string to be deserialized.
    Returns:
        any: The corresponding Python object.
    """
    return json.loads(my_str)

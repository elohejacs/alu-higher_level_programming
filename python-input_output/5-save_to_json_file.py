#!/usr/bin/python3
"""Task 5"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON.
    Args:
        my_obj (any): The object to be serialized to JSON.
        filename (str): The name of the file
        """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)

#!/usr/bin/python3
"""Task 6"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    Args:
        filename (str): The name of the file to load the JSON data.
        Returns:
        any: The Python object created from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

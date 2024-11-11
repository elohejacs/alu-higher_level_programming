#!/usr/bin/python3
"""The task 1"""

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    Args:
        filename (str): The name of the file to write.
        text (str): The string to write into the file.
        Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

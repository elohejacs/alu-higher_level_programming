#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file (UTF8) and rints it to stdout.
    Args:
        filename (str): The name of the file to be read.
        """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")

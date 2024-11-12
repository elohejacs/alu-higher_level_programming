#!/usr/bin/python3
"""Task 7 import sys and other files"""

import sys
from 5_save_to_json_file import save_to_json_file
from 6_load_from_json_file import load_from_json_file

"""TAsk 7 import sy and other files"""

filename = "add_item.json"

def main():
    """
    Adds all command-line arguments to a Python list and saves them
    The list is loaded from 'add_item.json' if it existsts are 
    appended. The updated list is saved back to the file.
    This script will:
    - Load the current list from 'add_item.json'.
    - Append command-line arguments (if any) to the list.
    - Save the updated list back to 'add_item.json'.
    """
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()

#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    index = 0
    while index < x:
        try:
            # Try to access the current index
            item = my_list[index]
            # Check if the item is an integer
            if isinstance(item, int):
                print("{:d}".format(item), end="")
                count += 1
        except IndexError:
            break  # Stop if the index is out of range
        index += 1  # Move to the next index

    print()  # Print a new line after printing integers
    return count

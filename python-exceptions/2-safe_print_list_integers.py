#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    count = 0
    index = 0

    while True:
        try:
            if index >= x:
                break  # Stop if we have printed 'x' elements

            # Try to print the current element
            print("{:d}".format(my_list[index]), end="")
            count += 1

        except (IndexError, ValueError) as e:
            # If IndexError occurs, break out of the loop
            if isinstance(e, IndexError):
                break  # Stop if the index is out of range
            # If ValueError occurs, just skip to the next index
            index += 1
            continue

        index += 1  # Increment the index for the next iteration

    print()  # Print a new line after printing integers
    return count

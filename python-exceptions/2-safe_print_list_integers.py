#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    
    count = 0
    index = 0
    
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
            count += 1
            index += 1
        except (IndexError, ValueError):
            # We catch IndexError and simply stop if we go out of range
            break
    
    print()  # Print a new line after printing integers
    return count

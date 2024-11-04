#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    
    count = 0
    
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (IndexError, ValueError):
            if i >= len(my_list):  # Check if we've gone beyond the length
                raise IndexError("Index out of range")
            continue
    
    print()
    return count

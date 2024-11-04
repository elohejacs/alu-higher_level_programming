#!/usr/bin/python3

def safe_print_list_integers(my_list=[], X=0):
    num = 0
    for items in range(X):
        try:
            print("{:d}".format(my_list(items)), end='')
            num += 1
        except (ValueError, TypeError):
            pass
    print()
    return num

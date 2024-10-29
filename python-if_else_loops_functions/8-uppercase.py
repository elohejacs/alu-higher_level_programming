#!/usr/bin/python3


def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            # Convert to uppercase by subtracting 32 from the ASCII value
            print(chr(ord(c) - 32), end="")
        else:
            print(c, end="")
    print()  # Print a new line at the end

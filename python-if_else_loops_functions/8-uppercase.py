#!/usr/bin/python3


def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:  # Check if character is lowercase
            char = chr(ord(char) - 32)  # Convert to uppercase
        print("{}".format(char), end="")
    print()  # Print a newline at the end

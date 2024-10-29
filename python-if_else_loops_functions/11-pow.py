#!/usr/bin/python3
def pow(a, b):
    result = 1.0  # Use a float for more precise division
    if b < 0:
        for _ in range(-b):
            result /= a
    else:
        for _ in range(b):
            result *= a
    return format(result, '.15g')  # Format to ensure precision

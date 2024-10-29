#!/usr/bin/python3
import sys


if __name__ == "__main__":
    num_args = len(sys.argv) - 1  # Exclude the script name from the count

    if num_args == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(num_args, "s" if num_args > 1 else ""))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, sys.argv[i]))

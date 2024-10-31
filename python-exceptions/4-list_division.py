#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            # Check if we are within the bounds of both lists
            value1 = my_list_1[i]
            value2 = my_list_2[i]
            try:
                result.append(value1 / value2)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)

    return result

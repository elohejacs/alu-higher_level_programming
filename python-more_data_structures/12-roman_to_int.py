#!/usr/bin/python3


def roman_to_int(roman_st):
    if not isinstance(roman_st, str) or roman_st is None:
        return 0

    roman_num = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    length = len(roman_st)

    for i in range(length):
        if i < length - 1 and roman_num[roman_st[i]] < roman_num[roman_st[i + 1]]:
            total -= roman_num[roman_st[i]]
        else:
            total += roman_num[roman_st[i]]

    return total

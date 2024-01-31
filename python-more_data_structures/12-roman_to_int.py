#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    r = 0
    romsum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romsub = {'V': "I", 'X': "I", 'L': "X", 'C': "X", 'D': "C", 'M': "C"}

    for i in range(len(roman_string)):
        r += romsum[roman_string[i]]

        if i > 0 and roman_string[i] != 'I' and \
                roman_string[i - 1] == romsub[roman_string[i]]:
            r -= romsum[roman_string[i - 1]] * 2

    return r

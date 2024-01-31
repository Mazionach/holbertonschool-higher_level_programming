#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    r = 0
    for i in range(len(roman_string)):
        if roman_string[i] == 'M':
            r += 1000
            if i > 0 and roman_string[i - 1] == 'C':
                r -= 200
        elif roman_string == 'D':
            r += 500
            if i > 0 and roman_string[i - 1] == 'C':
                r -= 200
        elif roman_string[i] == 'C':
            r += 100
            if i > 0 and roman_string[i - 1] == 'X':
                r -= 20
        elif roman_string[i] == 'L':
            r += 50
            if i > 0 and roman_string[i - 1] == 'X':
                r -= 20
        elif roman_string[i] == 'X':
            r += 10
            if i > 0 and roman_string[i - 1] == 'I':
                r -= 2
        elif roman_string[i] == 'V':
            r += 5
            if i > 0 and roman_string[i - 1] == 'I':
                r -= 2
        else:
            r += 1
    return r

#!/usr/bin/python3

def print_last_digit(number):
    last = number % 10 if number > 0 else 10 - number % 10
    print("{}".format(last), end="")
    return last

print_last_digit(-1)
print_last_digit(-803)

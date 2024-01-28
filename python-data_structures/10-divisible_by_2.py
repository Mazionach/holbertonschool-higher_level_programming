#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    r = list()

    for i in my_list:
        if i % 2 == 0:
            r += True
        else:
            r += False

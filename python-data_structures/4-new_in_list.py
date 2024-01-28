#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return copy(my_list)
    new = copy(my_list)
    new[idx] = element
    return new

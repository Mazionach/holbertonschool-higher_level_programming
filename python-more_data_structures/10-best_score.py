#!/usr/bin/python3

def best_score(a_dictionary):
    big = None
    if a_dictionary is None:
        return None
    for k in a_dictionary.keys():
        if big is None or a_dictionary[big] < a_dictionary[k]:
            big = k
    return big

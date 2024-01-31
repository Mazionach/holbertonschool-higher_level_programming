#!/usr/bin/python3

def best_score(a_dictionary):
    big = None

    for k in a_dictionary.keys():
        if big is None or big < a_dictionary[k]:
            big = a_dictionary[k]
    return big

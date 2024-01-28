#!/usr/bin/python3

def multiple_returns(sentence):
    r = [0, None]

    if len(sentence) > 0:
        r[0] = len(sentence)
        r[1] = sentence[0]

    return tuple(r)

#!/usr/bin/python3


def uppercase(str):
    for i in str:
        print("{}".format(chr(upChar(i))), end="")
    print("")


def upChar(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return ord(c) - 32
    else:
        return ord(c)

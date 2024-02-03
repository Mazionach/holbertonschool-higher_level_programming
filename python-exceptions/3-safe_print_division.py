#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        v = a / b
    except Exception:
        v = None
    finally:
        print("Inside result: {}".format(v))
        return v

#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for w in dir(hidden_4):
        if w[:2] != "__":
            print(w)

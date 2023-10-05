#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        return 1 / (a ** abs(b))
    else:
        return a ** b

#!/usr/bin/python3
def uppercase(str):
    for m in str:
        if ord(m) >= ord('a') and ord(m) <= ord('z'):
            char = chr(ord(m) - 32)
        else:
            char = m
        print("{:s}".format(char), end="")
    print('')

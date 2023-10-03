#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    for r in range(len(str)):
        if r != n:
            string += str[r]
    return string

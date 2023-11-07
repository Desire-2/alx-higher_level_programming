#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as f:
        for ln in f:
            print(ln, end="")
    f.closed

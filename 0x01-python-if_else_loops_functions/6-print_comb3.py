#!/usr/bin/python3
for r in range(0, 9):
    for w in range(r + 1, 10):
        if r == 8:
            print("{}{}".format(r, w))
        else:
            print("{}{}".format(r, w), end=", ")

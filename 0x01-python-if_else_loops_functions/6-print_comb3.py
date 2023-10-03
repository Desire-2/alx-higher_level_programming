#!/usr/bin/python3
for r in range(0, 9):
    for w in range(0, 10):
        if (r * 10 + w) == 89:
            print("{:02d}".format(r * 10 +  w))
        elif (r * 10 * w) < (w * 10 + r):
            print("{:02d}, ".format(r * 10 +  w), end=' ')

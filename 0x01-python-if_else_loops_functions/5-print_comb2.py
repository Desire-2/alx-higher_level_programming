#!/usr/bin/python3
for r in range(0, 100):
    if r == 99:
        print(r)
    else:
        print("{:0>2d}".format(r), end=", ")

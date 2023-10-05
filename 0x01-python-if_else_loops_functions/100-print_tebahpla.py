#!/usr/bin/python3
for r in range(122, 96, -1):
    print("{:s}".format(chr(r) if r % 2 == 0 else chr(r - 32)), end="")

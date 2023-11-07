#!/usr/bin/python3
"""
Module for log parsing scripts.
"""


import sys


if __name__ == "__main__":
    size = [0]
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def check_match(line):
        '''Checks for regexp match in line.'''
        try:
            line = line[:-1]
            words = line.split(" ")
            size[0] += int(words[-1])
            code = int(words[-2])
            if code in codes:
                codes[code] += 1
        except ValueError:
            pass

    def print_stats():
        '''Prints accumulated statistics.'''
        print("File size: {}".format(size[0]))
        for m in sorted(codes.keys()):
            if codes[m]:
                print("{}: {}".format(m, codes[m]))
    r = 1
    try:
        for line in sys.stdin:
            check_match(line)
            if r % 10 == 0:
                print_stats()
            r += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()

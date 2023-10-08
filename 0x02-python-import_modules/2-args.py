#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    r = len(sys.argv) - 1

    if r == 0:
        print("{} arguments.".format(r))
    elif r == 1:
        print("{} argument:".format(r))
    else:
        print("{} arguments:".format(r))

    if r >= 1:
        r = 0
        for arg in sys.argv:
            if r != 0:
                print("{}: {}".format(r, arg))
            r += 1

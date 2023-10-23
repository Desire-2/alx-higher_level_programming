#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    _total = 0
    for r in range(x):
        try:
            print("{}".format(my_list[r]), end="")
            _total += 1
        except IndexError:
            break
    print("")
    return (_total)

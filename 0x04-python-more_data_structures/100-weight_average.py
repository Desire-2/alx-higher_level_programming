#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    avg = 0
    s = 0
    for tup in my_list:
        avg += (tup[0] * tup[1])
        s += tup[1]
    return (avg / s)

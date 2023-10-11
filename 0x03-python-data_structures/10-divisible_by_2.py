#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nw_list = []
    for r in range(len(my_list)):
        if my_list[r] % 2 == 0:
            nw_list.append(True)
        else:
            nw_list.append(False)
    return nw_list

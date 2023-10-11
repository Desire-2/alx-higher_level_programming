#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        copy = my_list[:]
        copy[idx] = element
        return copy
    return my_list[:]

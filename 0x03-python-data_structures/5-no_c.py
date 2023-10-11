#!/usr/bin/python3
def no_c(my_string):
    nw_str = my_string.translate({ord(i): None for i in 'cC'})
    return nw_str

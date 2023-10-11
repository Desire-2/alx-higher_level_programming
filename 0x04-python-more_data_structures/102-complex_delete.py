#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for r, w in a_dictionary.items():
            if w == value:
                del a_dictionary[r]
                break

    return (a_dictionary)

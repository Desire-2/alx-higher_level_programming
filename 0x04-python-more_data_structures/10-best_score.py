#!/usr/bin/python3
def best_score(a_dictionary):
     if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    retn = list(a_dictionary.keys())[0]
    bigger = a_dictionary[ret]
    for r, w in a_dictionary.items():
        if w > bigger:
            bigger = w
            retn = r
    return (retn)

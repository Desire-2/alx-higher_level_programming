#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    _ret = list(a_dictionary.keys())[0]
    _big = a_dictionary[_ret]
    for k, v in a_dictionary.items():
        if v > _big:
            _big = v
            _ret = k
    return (_ret)

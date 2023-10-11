#!/usr/bin/python3
def to_subtract(list_num):
    _to_sub = 0
    _max_list = max(list_num)

    for n in list_num:
        if _max_list > n:
            _to_sub += n

    return (_max_list - _to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    _rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(_rom_n.keys())

    nm = 0
    _last_rom = 0
    _list_num = [0]

    for c in roman_string:
        for _r_num in list_keys:
            if _r_num == c:
                if _rom_n.get(c) <= _last_rom:
                    nm += to_subtract(_list_num)
                    _list_num = [_rom_n.get(c)]
                else:
                    _list_num.append(_rom_n.get(c))

                _last_rom = _rom_n.get(c)

    nm += to_subtract(_list_num)

    return (nm)

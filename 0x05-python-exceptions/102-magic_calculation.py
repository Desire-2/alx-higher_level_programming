#!/usr/bin/python3

def magic_calculation(a, b):
    _rslt = 0
    for r in range(1, 3):
        try:
            if r > a:
                raise Exception("Too far")
            else:
                _rslt += (a**b)/r
        except Exception:
            _rslt = b + a
            break
    return (_rslt)

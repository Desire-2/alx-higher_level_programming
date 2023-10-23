#!/usr/bin/python3
def safe_print_division(a, b):
    _div = None
    try:
        _div = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(_div))
        return _div

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    _rslt = []
    for r in range(list_length):
        _div = 0
        try:
            _div = my_list_1[r] / my_list_2[r]
        except (TypeError, ValueError):
            print("wrong type")
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (IndexError, ValueError):
            print("out of range")
        finally:
            _rslt.append(_div)
    return _rslt

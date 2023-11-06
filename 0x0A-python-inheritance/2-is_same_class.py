def is_same_class(obj, a_class):
    """Checks if obj is exactly an instance of a_class"""

    return type(obj) is a_class

# Test the is_same_class function
a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))

#!/usr/bin/python3
"""instance of a class that inherited from, the specified class"""


def is_kind_of_class(obj, a_class):
    """checks if an object is an inherited instance of a class.

    Args:
        obj : The object
        a_class (type): The class to check.
    Returns:
        True:If obj is an instance or inherited instance
        False:
    """
    if isinstance(obj, a_class):
        return True
    return False

#!/usr/bin/python3
"""Defines a function tha vhecks an inherited class"""


def inherits_from(obj, a_class):
    """Checks if  object is an inherited instance .

    Args:
        obj : The object
        a_class: The class
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

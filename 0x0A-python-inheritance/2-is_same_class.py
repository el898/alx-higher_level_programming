#!/usr/bin/python3
""" a  function that checks claSS"""


def is_same_class(obj, a_class):
    """CheckS if  object is  an instance of a class.

    Args:
        obj : The object
        a_class (type): The given class to match.
    Returns:
        true: If obj is exactly an instance of the specified a_class
        false: else
    """
    if type(obj) == a_class:
        return True
    return False

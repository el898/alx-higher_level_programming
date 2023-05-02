#!/usr/bin/python3
"""Defines the addition of two integers."""


def add_integer(a, b=98):
    """
    Returns the addition of a and b

    Args:
        a: first integer
        b: second integer

    Raises:
        TypeError: If either of a or b is a non-integer or non-float.
    """
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer or a float")
    if (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer or a float")
    return int(a) + int(b)

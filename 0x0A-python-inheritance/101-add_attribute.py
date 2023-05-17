#!/usr/bin/python3
"""function that adds a new attribute to an object"""


def add_attribute(obj, att, value):
    """Check if Object can’t have new attribute.

    Args:
        obj: The object.
        att (str): The name of the attribute .
        value (any): The value.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

#!/usr/bin/python3
""" a class BaseGeometry (based on 6-base_geometry.py).."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """area of base geometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): name of the parameter
            value (int): parameter to validate
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

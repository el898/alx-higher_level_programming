#!/usr/bin/python3

"""
a magic class
"""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass instance.

        Args:
            radius (float or int): The radius of the new MagicClass.
        """

        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Return the area of a ircle:."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):

        """Calculate and Return The circumference of the MagicClass."""

        return (2 * math.pi * self.__radius)

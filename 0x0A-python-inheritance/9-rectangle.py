#!/usr/bin/python3
"""a class Rectangle that inherits a base geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle"""

    def __init__(self, width, height):
        """Intialize the new Rectangle.

        Args:
            width: Rectangle width.
            height: Rectangle height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str()."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

#!/usr/bin/python3
"""Defines Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a  Rectangle.

        Args:
            width: The width of the  Rectangle.
            height: The height of the Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

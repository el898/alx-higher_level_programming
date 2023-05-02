#!/usr/bin/python3
""" class Square that inherits from Rectangle (9-rectangle.py"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square class."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size: integer size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

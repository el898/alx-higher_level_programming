#!/usr/bin/python3

"""Define a Square."""


class Square:
    """for the square."""

    def __init__(self, size=0):
        """
        Initialize a Square instance.
        Args:
            size (int): The Default size is 0.

        """
        self.size = size

    @property
    def size(self):
        """Getter:gets the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns:The area of the square."""
        return (self.__size ** 2)

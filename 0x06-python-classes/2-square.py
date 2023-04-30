#!/usr/bin/python3
"""Define a Square"""


class Square:
    """for the square"""

    def __init__(self, size=0):
        """
        Args:
            size(int): size of the new square.

        Raises:
            TypeError: if size is not an int.
            ValueError: if size < 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

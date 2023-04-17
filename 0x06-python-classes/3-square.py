#!/usr/bin/python3

class Square:
    """Define the class square"""
    def __init__(self, size=0):
        """
        Initialize a Square instance.

        Args:
            size (int): The Default size is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns:The area of the square."""
        return (self.__size ** 2)

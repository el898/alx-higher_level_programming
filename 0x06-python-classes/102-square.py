#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """ a square class."""

    def __init__(self, size=0):
        """represent a  square instance.
        Args:
            size (int): The size of the  square.
        """
        self.__size = size

    @property
    def size(self):
        """Getter: get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Define the == comparison to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """ >= comparison to a Square instance."""
        return self.area() >= other.area()

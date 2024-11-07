#!/usr/bin/python3
"""This module defines the Square class"""


from 9-rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle and implements specific behavior."""

    def __init__(self, size):
        """Initializes the Square with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns the string description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)

#!/usr/bin/python3
"""
This module defines the Square class, which inherits from Rectangle.
"""

class BaseGeometry:
    """BaseGeometry class with methods integer validation."""

    def area(self):
        """Raises an exception if the area method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class that inherits area calculation."""

    def __init__(self, width, height):
        """Initializes the Rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string description of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class that inheri specific behavior."""

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

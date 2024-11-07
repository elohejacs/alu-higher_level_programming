#!/usr/bin/python3
"""This module defines the Rectangle class"""

class BaseGeometry:
    """BaseGeometry can area method that raises an exception."""
    def area(self):
        """Raises an exception method is not implemented."""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Validates that the value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""
    
    def __init__(self, width, height):
        """Initialize the Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

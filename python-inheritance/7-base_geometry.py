#!/usr/bin/python3
"""This module defines class"""


class BaseGeometry:
    """BaseGeometry class with integer validation."""

    def area(self):
        """Raises an exception if the area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

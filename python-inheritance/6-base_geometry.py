#!/usr/bin/python3
"""
This module defines the Basegeometry class
that raises an exception if not implemented.
"""


class BaseGeometry:
    """A class representing basic geometry."""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

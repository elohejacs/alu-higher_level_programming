#!/usr/bin/python3
"""module defines a rectangle with width and height attributes"""


class Rectangle:
    """Represents a rectangle and"""

    # Public class attribute
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes new Rectangle instance with width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle using '#'."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr(self):
        """Returns a string representation for recreating a new instance."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints message when Rectangand updates instance count."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

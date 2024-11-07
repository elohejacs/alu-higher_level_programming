#!/usr/bin/python3
"""This module defines the Square class"""


class BaseGeometry:
    """BaseGeometry class with an area method that raises an exception."""   
    def area(self):
        """Raises an exception if the area method is not implemented."""
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
        """Initialize the Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle (width * height)."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class that inherits from Rectangle."""
    def __init__(self, size):
        """Initialize the Square with validated size."""
        self.integer_validator("size", size)
        
        # Call the parent class constructor with size as both width and height
        super().__init__(size, size)

    def area(self):
        """Return the area of the square (size * size)."""
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """Return a string representation of the Square."""
        return "Rectangle".format(self._Rectangle__width, self._Rectangle__height)

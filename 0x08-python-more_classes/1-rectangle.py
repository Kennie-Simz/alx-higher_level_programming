#!/usr/bin/python3
"""
Module defines a class rectangle
"""


class Rectangle:
    """
    this class has two attributes
    - width
    - height
    """
    def __init__(self, width=0, height=0):
        """
        Creates width and height attributes
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        To return width if setter checks pass
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Validates if value >= 0,
        Raise:
            TypeError
            ValueError
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        To return height if setter checks pass
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Validates if value >= 0,
        Raises:
            TypeError
            ValueError
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

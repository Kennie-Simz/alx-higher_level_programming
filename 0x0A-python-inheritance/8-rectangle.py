#!/usr/bin/python3
"""
This module contains a class
with a public instance and
Raises:
    Exception when required
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle with private height and width
    """
    def __init__(self, width, height):
        """
        instation of class
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

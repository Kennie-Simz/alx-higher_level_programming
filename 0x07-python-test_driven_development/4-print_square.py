#!/usr/bin/python3
"""
Module function for printing squares
"""


def print_square(size):
    """
    prints square of a given size
    Raises:
        TypeError:
        ValueError:
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    print("{}\n".format("#" * size) * size, end="")

#!/usr/bin/python3
"""
Module that adds two integers and returns sum of two numbers a & b.
Only accepts integers and floats, else raise TypeError
Also converts float to integer
"""


def add_integer(a, b=98):
    """
    add_integer: Check input if correct, cast both into ints and return sum
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')
    elif isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')
    return(int(a) + int(b))

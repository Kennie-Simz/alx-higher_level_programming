#!/usr/bin/python3
import json
"""
File contains function that returns
JSON representation of an object
"""


def to_json_string(my_obj):
    """
    Function to return JSON representation
    """
    return (json.dumps(my_obj))

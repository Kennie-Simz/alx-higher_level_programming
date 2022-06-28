#!/usr/bin/python3
"""
Module that prints text with 2 newlines after character - . ? and :
"""


def text_indentation(text):
    """
    function prints text and 2 new lines
    """
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError('text must be a string')
    string = "".join([a if a not in ".?:" else a + "\n\n" for a in text])
    print("\n".join([x.strip() for x in string.split("\n")]), end="")

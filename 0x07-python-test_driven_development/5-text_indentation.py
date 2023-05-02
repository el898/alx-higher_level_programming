#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """gives two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text.
    Raises:
        TypeError: text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c = c + 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c = c + 1
            while c < len(text) and text[c] == ' ':
                c = c + 1
            continue
        c = c + 1

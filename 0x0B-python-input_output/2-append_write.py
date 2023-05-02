#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends and  returns the number of characters added
    Args:
        filename : The name of the file
        text: The string to append to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

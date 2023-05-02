#!/usr/bin/python3
"""
defines function that reads a text file
"""


def read_file(filename=""):
    """this function reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

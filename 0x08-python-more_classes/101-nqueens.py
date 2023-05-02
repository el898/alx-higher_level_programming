#!/usr/bin/python3
"""N Queens Script"""


import sys

if __name__ == "__main__":

    arguments = sys.argv
    if (len(arguments) != 2):
        print("Usage: nqueens N")
        exit(1)
    try:
    n = int(arguments[1])
    except ValueError:
        n = ''

    if (not isinstance(n, int)):
        print("N must be a number")
        exit(1)

    if (n < 4):
        print("N must be at least 4")
        exit(1)

#!/usr/bin/python3
"""    Function to read the given file"""


def read_file(filename=""):
    """Using with statement to open in reading mode"""
    with open(filename, 'r') as f:
            print(f.read())

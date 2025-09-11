#!/usr/bin/python3
"""    Function to read the given file"""


def read_file(filename=""):
    """Using with statement to open and read file in writing and reading mode"""
    with open(filename, '+w') as f:
        for line in f:
            print(line)



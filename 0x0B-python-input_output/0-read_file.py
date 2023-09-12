#!/usr/bin/python3
"""Contains the read_file function"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

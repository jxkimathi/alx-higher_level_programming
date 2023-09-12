#!/usr/bin/python3
"""Contains the append_write function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a textfile"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

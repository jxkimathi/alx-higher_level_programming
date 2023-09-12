#!/usr/bin/python3
"""Contains the function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line after a certain string in a textfile"""
    with open(filename, "r", encoding="utf-8") as f:
        listt = []
        while True:
            line = f.readline()
            if line == "":
                break
            listt.append(line)
            if search_string in line:
                listt.append(new_string)
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(listt)

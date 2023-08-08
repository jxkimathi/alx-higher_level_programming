#!/usr/bin/python3
"""Prints the lowercase alphabet minus q and e"""
for index in range(97, 123):
    if chr(index) != 'q' and chr(index) != 'e':
        print("{}".format(chr(index)), end="")

#!/usr/bin/python3
"""Prints out whether number is positive, zero or negative"""
import random
number = random.randint(-10, 10)
if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")

#!/usr/bin/python3
"""Prints fizz if num % 3 == 0, buzz if num % 5 == 0
   and fizzbuzz if num % 3 and num % 5 == 0"""


def fizzbuzz():
    for index in range(0, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("FizzBuzz ", end="")
        elif index % 3 == 0:
            print("Fizz ", end="")
        elif index % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(index), end="")

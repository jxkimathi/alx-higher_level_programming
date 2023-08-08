#!/bin/bash
"""Prints the numbers from 0 to 99"""
for index in range(0, 100):
    if index == 99:
        print("{}".format(index))
    else:
        print("{:02}".format(index), end=", ")

#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the length of a string"""
    tuple = ()
    if len(sentence) == 0:
        tuple = 0, "None"
    else:
        tuple = len(sentence), sentence[0]
        return tuple

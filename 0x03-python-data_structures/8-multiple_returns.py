#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the length of a string"""
    if len(sentence) == 0:
        sentence = 0, "None"
    else:
        sentence = len(sentence), sentence[0]
        return sentence

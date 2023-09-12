#!/usr/bin/python3
"""Contains the class_to_json function"""
import json


def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    return obj.__dict__

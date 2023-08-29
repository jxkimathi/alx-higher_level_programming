#!/usr/bin/python3
from __future__ import print_function


def safe_function(fct, *args):
    """Executes a function safely"""
    import sys
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return result

#!/usr/bin/bash
def magic_calculation(a, b):
    """Prints the same thing as the ByteCode"""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)

        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        return (sub(a, b))
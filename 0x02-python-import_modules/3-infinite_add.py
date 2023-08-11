#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the result of the addition of all arguments"""
    from sys import argv
    total = 0
    for index in argv[1:]:
        total = total + int(index)
    print("{:d}".format(total))

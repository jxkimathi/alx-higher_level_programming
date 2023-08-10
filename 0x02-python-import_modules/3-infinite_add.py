#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the result of the addition of all arguments"""
    import sys

    total = 0

    for index in range(len(sys.argv) - 1):
        total = total + int(sys.argv[index + 1])
    print("{}".format(total))

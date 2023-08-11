#!/usr/bin/python3
if __name__ == "__main__":
    """Prints all names defined in the compile module hidden_4.pyc"""

    import hidden_4

    for name in dir(hidden_4):
        if name[:2] != "__":
            print("{:s}".format(name))

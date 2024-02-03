#!/usr/bin/python3
"""Displays the body of the response"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.arv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as err:
        print("Error code:", err.code)

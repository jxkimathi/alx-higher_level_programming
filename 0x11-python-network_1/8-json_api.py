#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""


import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = res.json()
        if response == {}:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

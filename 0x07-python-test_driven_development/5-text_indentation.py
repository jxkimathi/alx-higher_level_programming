#!/usr/bin/python3

def text_indentation(text):
    """Prints a text with 2 new lines after: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    prev_char = ''
    for char in text:
        if char in ['.', '?', ':']:
            print(char + "\n")
        else:
            if prev_char not in ['.', '?', ':']:
                print(char, end="")
            else:
                print('' + char, end="")
        prev_char = char
    print()

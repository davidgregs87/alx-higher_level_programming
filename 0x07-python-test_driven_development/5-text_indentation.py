#!/usr/bin/python3
"""
Program that Ident a text according to '.' and '?' symbol
"""


def text_indentation(text):
    """  function that prints a text with 2 new lines after
    each of these characters: ., ?
    """
    if (type(text) is not str or text is None):
        raise TypeError("text must be a string")
    flag = 0
    for c in text:
        if (c == '.' or c == '?' or c == ':'):
            print(c, end='')
            print('')
            print('')
            flag = 1
        else:
            if (flag == 0):
                print(c, end='')
            else:
                if (c == ' ' or c == '\t'):
                    pass
                else:
                    print(c, end="")
                    flag = 0

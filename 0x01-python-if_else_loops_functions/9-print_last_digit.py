#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number *= -1
    ldigit = number % 10
    print("{:d}".format(ldigit), end="")
    return ldigit

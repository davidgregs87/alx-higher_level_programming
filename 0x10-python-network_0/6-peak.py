#!/usr/bin/python3
"""This Module is to find the peak of numbers"""


def find_peak(list_of_integers):
    """Write a function that finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return
    temp = list_of_integers[0]
    for i in range(1, len(list_of_integers)):
        if temp < list_of_integers[i]:
            temp = list_of_integers[i]
            return temp

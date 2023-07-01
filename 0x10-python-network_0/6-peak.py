#!/usr/bin/python3
"""This Module is to find the peak of numbers"""


def find_peak(list_of_integers):
    """Write a function that finds a peak in a list of unsorted integers."""
    num = sorted(list_of_integers, reverse=True)
    return(num[0])

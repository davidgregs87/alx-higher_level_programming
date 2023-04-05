#!/usr/bin/python3
""" Program that sort a list int """


class MyList(list):
    """ class that inherist from list """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        new_list = self[:]
        new_list.sort()
        print(new_list)

#!/usr/bin/python3
""" Program that validate if an object belongs to a sublcass """


def inherits_from(obj, a_class):
    """ function that returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False. """
    if (type(obj) == a_class):
        return False
    return isinstance(obj, a_class)

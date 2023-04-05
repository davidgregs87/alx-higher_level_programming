#!/usr/bin/python3
""" Program that checks if a class is the same
object os inherit from """


def is_kind_of_class(obj, a_class):
    """  function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False. """
    return (isinstance(obj, a_class))

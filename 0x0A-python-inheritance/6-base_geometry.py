#!/usr/bin/python3
""" Empty Geometry Class """


class BaseGeometry:
    """ class that improve geometry"""
    def area(self):
        """ raises an Exception with the message area() is not implemented """
        raise Exception("area() is not implemented")

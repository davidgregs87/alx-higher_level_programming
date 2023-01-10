#!/usr/bin/python3
"""Pascal Triangle."""


def pascal_triangle(n):
    """A function that returns a list of lists of integers representing
    the Pascal triangle.

    Args:
        n (int):    The list of Integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        tmp = [1]
        for x in range(len(tri) - 1):
            tmp.append(tri[x] + tri[x + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle

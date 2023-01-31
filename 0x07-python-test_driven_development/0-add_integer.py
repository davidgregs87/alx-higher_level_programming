def add_integer(a, b=98):
    """
    Adds the input integers
    """
    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)
    if not ((type(a) is int) or (type(a) is float)):
        raise TypeError('a must be an integer')
    if not ((type(b) is int) or (type(b) is float)):
        raise TypeError('b must be an integer')
    return (a + b)
    

print(add_integer(4, -50))

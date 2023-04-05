===============================
 Testing module 7-base_geometry.py
===============================

``area(self)`` raise a Exception
``integer_validator(self, name, value)`` validates the input value

Initial
=======

First, Import module and function

        >>> BaseGeometry = __import__('7-base_geometry').BaseGeometry

Use:

	>>> bg = BaseGeometry()

validate functions

	>>> 'area' in dir(BaseGeometry)
	True

	>>> 'integer_validator' in dir(BaseGeometry)
	True

Validate instance

	 >>> dir(bg) == dir(BaseGeometry)
    	 True

Validate area function

	 >>> bg.area()
	 Traceback (most recent call last):
  	 ...
	 Exception: area() is not implemented

Validate integer_validator

	 >>> bg.integer_validator("name", -10)
	 Traceback (most recent call last):
  	 ...
	 ValueError: name must be greater than 0

	 >>> bg.integer_validator("name", 0)
	 Traceback (most recent call last):
	 ...
	 ValueError: name must be greater than 0

	 >>> bg.integer_validator("name", 4)

	 >>> bg.integer_validator("name", "last")
	 Traceback (most recent call last):
  	 ...
	 TypeError: name must be an integer

Boolean type

	 >>> bg.integer_validator("name", True)
    	 Traceback (most recent call last):
    	 ...
    	 TypeError: name must be an integer

List type

	 >>> bg.integer_validator("Test", [3])
    	 Traceback (most recent call last):
    	 ...
    	 TypeError: Test must be an integer

Tuple type

         >>> bg.integer_validator("Test", (4, ))
    	 Traceback (most recent call last):
    	 ...
    	 TypeError: Test must be an integer

Set type

	 >>> bg.integer_validator("Test", {3, 4})
    	 Traceback (most recent call last):
    	 ...
    	 TypeError: Test must be an integer

Dict type

         >>> bg.integer_validator("Test", {1: 2})
    	 Traceback (most recent call last):
    	 ...
    	 TypeError: Test must be an integer

with None

         >>> bg.integer_validator("Test", None)
    	 Traceback (most recent call last):
    	 ...
    	 TypeError: Test must be an integer

	 >>> bg.integer_validator()
	 Traceback (most recent call last):
	 ...
	 TypeError: integer_validator() missing 2 required positional arguments: 'name' and 'value'

	 >>> bg.integer_validator(1)
	 Traceback (most recent call last):
 	 ...
	 TypeError: integer_validator() missing 1 required positional argument: 'value'

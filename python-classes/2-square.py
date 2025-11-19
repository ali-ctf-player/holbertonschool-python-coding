#!/usr/bin/python3
"""It is about class tutorial"""


class Square:
    """It is inside of class"""

    def __init__(self, size=0):
        """It is inside of function"""

        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

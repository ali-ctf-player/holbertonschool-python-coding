#!/usr/bin/python3
"""This is a class tutorial"""


class Square:
    """It is inside of class named Square"""

    def __init__(self, size=0):
        """It is inside of function named initialization"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

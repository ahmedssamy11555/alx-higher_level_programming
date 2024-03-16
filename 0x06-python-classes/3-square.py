#!/usr/bin/python3
"""" Module for a class defines a square"""


class Square:
    """class defines a square"""
    def __init__(self, size=0):
        """function initializes the class square

           Parameters:
           self (obj): the instance of the class
           size (int): the size of the square
           """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """"Returns the area of the square
            parameters:
            self (obj): the instance of the class
            :return: area (int): the area of the square
        """
        return self.__size ** 2

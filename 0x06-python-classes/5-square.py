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
        self.__size = size

    @property
    def size(self):
        """"Returns the size of the square
            parameters:
            self (obj): the instance of the class
            :return: size (int): the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """"Returns the area of the square
                parameters:
                self (obj): the instance of the class
                value (int): the new size value
                return: updated_size (int)
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """"Returns the area of the square
            parameters:
            self (obj): the instance of the class
            :return: area (int): the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """"prints the square in # using it's size
                   parameters:
                   self (obj): the instance of the class
        """
        if self.size == 0:
            print()
        for _ in range(self.__size):
            for _ in range(self.__size - 1):
                print("#", end="")
            print("#")

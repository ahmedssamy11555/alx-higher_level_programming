#!/usr/bin/python3
"""" Module for a class defines a square"""


class Square:
    """class defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """function initializes the class square

           Parameters:
           self (obj): the instance of the class
           size (int): the size of the square
           """
        self.__size = size
        self.__position = position

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
        if self.__size == 0:
            print()
            return

        offset_y = self.__position[1]

        for _ in range(offset_y):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    @property
    def position(self):
        """"gets the position value
                 parameters:
                 self (obj): the instance of the class
        """
        return self.__position

    @position.setter
    def position(self, value):
        """"sets the position value
                    parameters:
                    self (obj): the instance of the class
                    value (tuple): position
        """
        if isinstance(value, tuple) and len(value) == 2:
            if all(isinstance(item, int) and item >= 0 for item in value):
                self.__position = value
                return
        raise TypeError("position must be a tuple of 2 positive integers")

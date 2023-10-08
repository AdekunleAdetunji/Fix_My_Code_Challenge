#!/usr/bin/python3

"""
This module contains a python class called square that
returns the area and height of the rectangle
"""


class square():
    """
    Square class
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize a square instance"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Return the perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return the string representation of the object"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

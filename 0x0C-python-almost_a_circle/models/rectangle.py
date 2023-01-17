#!/usr/bin/python3
"""Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Class Models a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """height getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate area of rectangle"""
        return (self.width * self.height)

    def display(self):
        """Print rectangle instance with '#'"""
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for _ in range(self.__height)))

    def __str__(self):
        """Returns rect instance string rep"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y,
                   self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the class Rectangle by adding the public method"""
        for a, arg in enumerate(args):
            if a == 0:
                self.id = arg
            if a == 1:
                self.width = arg
            if a == 2:
                self.height = arg
            if a == 3:
                self.x = arg
            if a == 4:
                self.y = arg

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

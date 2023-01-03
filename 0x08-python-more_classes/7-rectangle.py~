#!/usr/bin/python3
"""Rectangle Module."""


class Rectangle:
    """Defines a rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize arectangle.
        args:
        width: int, initialized to 0
        height: int, initialized to 0
        exceptions:
        TypeError: height & width must be ints
        ValueError: height & width must be >= 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves valus of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width value"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Retrieves value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height value"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """print rectangle with char #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')
        return ("".join(rect))

    def __repr__(self):
        """Return string representation of rectangle"""
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """Print message when instance is deleted"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

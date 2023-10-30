#!/usr/bin/python3
"""defining a rectangle based on 4-rectangle.py"""

class Rectangle:
    """string representation of a rectangle"""

    # Class-level variable to keep track of the number of instances created
    number_of_instances = 0

    # Symbol to be used for printing the rectangle
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        # Initialize the Rectangle with specified width and height
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        # Getter method for retrieving the width of the rectangle
        return self.__width

    @width.setter
    def width(self, value):
        # Setter method to set the width of the rectangle
        self.__width = value
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        # Getter method for retrieving the height of the rectangle
        return self.__height

    @height.setter
    def height(self, height):
        # Setter method to set the height of the rectangle
        self.__height = height
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

    def area(self):
        # Calculate the area of the rectangle
        return self.__width * self.__height

    def perimeter(self):
        # Calculate the perimeter of the rectangle
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        # String representation of the rectangle
        total = ""
        if self.__height == 0 or self.__width == 0:
            return total
        for i in range(self.__height):
            total += (str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                total += "\n"
        return total

    def __repr__(self):
        # Representation of the rectangle object
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        # Method called when the object is deleted

        print("Bye rectangle...")

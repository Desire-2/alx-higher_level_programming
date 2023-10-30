class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 0 if self.width == 0 or self.height == 0 else (self.width + self.height) * 2

    def __str__(self):
        return "\n".join(["#" * self.width for _ in range(self.height)]) if self.width != 0 and self.height != 0 else ""

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

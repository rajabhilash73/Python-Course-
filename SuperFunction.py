"""
super() = Super () function used to give access to the methods of the parent class.
Returns a temporary objects of a parent class when used.
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        # self.length = length
        # self.width = width
       super().__init__(length, width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        # self.length = length
        # self.width = width
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

square = Square(4, 4)
cube = Cube(8, 6, 12)

print(square.area())
print(cube.volume())


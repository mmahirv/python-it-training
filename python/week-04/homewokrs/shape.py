__author__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def calculate_area(self):
        return self.width * self.height
    
class Square(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def calculate_area(self):
        return self.width * self.height

first_rectangle = Rectangle(5, 10)
print(f"Area of the rectangle: {first_rectangle.calculate_area()}")

first_square = Square(4, 4)
print(f"Area of the square: {first_square.calculate_area()}")
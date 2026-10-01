__author__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    

first_rectangle = Rectangle(5, 7)
    
print(f"Area of the rectangle: {first_rectangle.area()} ")
print(f"Perimeter of the rectangle: {first_rectangle.perimeter()} ")
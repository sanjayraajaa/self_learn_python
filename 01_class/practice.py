class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print(f"Area: {self.length * self.width}")
    
    def perimeter(self):
        print(f"Perimeter: {2 * (self.length + self.width)}")
    
    def all_values(self):
        self.area()
        self.perimeter()

r1 = Rectangle(10,5)
r1.all_values()
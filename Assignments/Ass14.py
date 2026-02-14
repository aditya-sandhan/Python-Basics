'''Create a class Shape with a method area().
Create subclasses Circle, Rectangle, and Triangle 
that override the area() method'''

class Shape:
    pi = 3.14
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,r):       # storing parameters in constructor to maintain polymorphism 
        self.r = r
    
    def area(self):
        print(f"Area of Circle = {Shape.pi * self.r * self.r}")

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        print(f"Area of rectangle = {self.l*self.b}")

class Triangle(Shape):
    def __init__(self,b,h):
        self.b = b
        self.h = h

    def area(self):
        print(f"Area of Triangle = {0.5 *self.b*self.h}")


shapes = [Circle(3),Rectangle(4,5),Triangle(6,7)]

for x in shapes:
    x.area()
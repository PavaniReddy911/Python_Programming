from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod   
    def area(self):
        pass


class rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth


class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

rect = rectangle(10, 5)
circle = circle(7)


print("Area of Rectangle:", rect.area())
print("Area of Circle:", circle.area())

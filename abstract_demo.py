'''
Create an Abstract Base Class called Shape that include
 abstract methods area() and circumference().
Then derive two classes Circle and Rectangle from
the Shape class and implement the area() and
circumference() methods . Write a Python program to implement above concept.
'''
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def circumference(self):
        pass
class Circle(Shape):
    def area(self):
        print("The area of circle is computed here")
    def circumference(self):
        print("The circumference of circle is computed here")
class Rectangle(Shape):
    def area(self):
        print("The area of rectangle is computed here")
    def circumference(self):
        print("The circumference of rectangle is computed here")
circle = Circle()
rectangle = Rectangle()
circle.area()
rectangle.area()
circle.circumference()
rectangle.circumference()

from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def printArea(self):
        return 0
class Rectangle(Shape):
    type="Rectangle"
    sides=4

    def __init__(self):
        self.length=5
        self.breadth=7

    #this is must method.
    def printArea(self):
        print (f"Area: {self.length+self.breadth}")

rect = Rectangle()

rect.printArea()

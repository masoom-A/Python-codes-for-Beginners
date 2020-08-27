from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def printareas(self):
        return 0
class rect(shape):
    def __init__(self):
        self.length=6
        self.breadth=7
    def printareas(self):
        return (self.length*self.breadth)
rect1=rect() #creating object
print(rect1.printareas())
        

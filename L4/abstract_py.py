from abc import ABC, abstractmethod
class Vehicle(ABC):  # Abstract class bec it inhert from abc  so You cannot create an object directly from Vehicle calss.
    @abstractmethod
    def start_engine(self):#self refers to the current object.
        pass #pass means "do nothing for now" no current implementation but any class inhert must implement all abstract methods
    @abstractmethod
    def stop_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
    def stop_engine(self):
        print("Car engine stopped")
# vehicle = Vehicle()  # TypeError: Can't instantiate abstract class
car = Car()
car.start_engine()  # Output: Car engine started
car.stop_engine()   # output: car engine stoped



# another exapmle ""Interface-like Pattern""
class Swimmable:
    def swim(self):
        pass
class Flyable:
    def fly(self):
        pass
class Duck(Swimmable, Flyable):
    def swim(self):
        print("Duck swimming")
    def fly(self):
        print("Duck flying")
duck = Duck()
duck.swim()
duck.fly()

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    @abstractmethod
    def start_engine(self):
        pass
    def stop_engine(self):
        pass


# Inheritance + Encapsulation 
class Car(Vehicle):
    def __init__(self, brand, model, speed=0): # this is speed default value if user does not enter a value 
        super().__init__(brand, model)
        self.__speed = speed     # Private attribute (Encapsulation)

    # Getter
    def get_speed(self):
        return self.__speed

    # Setter
    def set_speed(self, speed):
        if speed >= 0:
            self.__speed = speed
        else:
            print("Speed cannot be negative")
    def stop_engine(self):
        print(f"{self.brand} {self.model} engine stopped ")        

    # Method
    def accelerate(self, value):
        self.__speed += value
        print(f"Car accelerated. Current speed: {self.__speed}")

    # Polymorphism : using same method but with diff implementation
    def start_engine(self):
        print(f"{self.brand} {self.model} engine started ")


#  Main Class 
class Main:
    @staticmethod # Allows running the method without creating object.
    def run():
        car1 = Car("Toyota", "Corolla")

        car1.start_engine()
        car1.set_speed(50)
        print("Current speed:", car1.get_speed())

        car1.accelerate(20)
        car1.stop_engine()


# Run program
if __name__ == "__main__": # makesure that file will be excuted only if this file main run 
    Main.run()

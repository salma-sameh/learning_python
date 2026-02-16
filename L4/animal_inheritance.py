class Animal: 
  def __init__(self, name): 
    self.name = name 
  def make_sound(self): 
    print("Generic animal sound") 
class Dog(Animal): 
  def __init__(self, name, breed): # breed النوع
    super().__init__(name) # Call superclass constructor 
    self.breed = breed 
  def make_sound(self): 
    print("Woof! Woof! Woof! Woof!") 
myDog = Dog("Buddy", "Labrador") 
myDog.make_sound() # Output: Woof!

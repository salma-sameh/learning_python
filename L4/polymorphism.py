class Animal: #Python automatically creates a default constructor
  def make_sound(self): 
    pass # Abstract method - subclasses must define it 
class Dog(Animal): 
  def make_sound(self): 
    print("Woof!") 
class Cat(Animal): 
  def make_sound(self): 
    print("Meow!") 

#make a function that take object and call the make_sound fuction through the given object
def make_animal_sound(animal): 
  animal.make_sound() # Polymorphic call 
myDog = Dog("Buddy") 
myCat = Cat("Whiskers") 
make_animal_sound(myDog) # Output: Woof! 
make_animal_sound(myCat) # Output: Meow!

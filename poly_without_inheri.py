class Animal:
    alive = True
    
class Dog(Animal):
    def bark(self):# a subclass of animal that defines the bark method
        print("Woof!")    
        
class Cat(Animal):
    def bark(self):
        print("Meow!") 

class Fish(Animal):
    def bark(self):
        print("Blub!")
        
class Car:
    alive = True
    def bark(self):
        print("Honk!")
        
# list of animals
animals = [Dog(), Cat(), Fish(), Car()]

# loop through the list of animals
for animal in animals:
    animal.bark()
    print(animal.alive)                                  
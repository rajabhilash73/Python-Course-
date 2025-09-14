"""
Inheritance = inheritance is a fundamental concept in object-oriented programming
that allows one class(child class/derived class) to inherits the attributes and method of another
class(parents class/base class).

The children classes will inherit everything that parent class have.
"""
class Animal:
    
    alive = True
    def eat(self):
        print("This animal is eating.")
        
    def slumber(self):
        print("This animal is sleeping.")
        
class Rabbit(Animal):
    def run(self):
        print("The rabbit is running")   

class Lion(Animal):
    def roar(self):
        print("The lion is roaring")        

class Elephant(Animal):
    def climb(self):
        print("The elephant is climbing")

rabbit = Rabbit()
lion = Lion()
elephant = Elephant()

# print(rabbit.alive)
# lion.eat()
# elephant.climbing()

rabbit.run()
lion.roar()
elephant.climb()
     

"""
Multi - Level Inheritance = When a derived (child) class inherits another derived (child) class.
"""
class Organisms:     # This organisms class is parent of parent class that is grandparents of child class.
    alive = True

class Animal(Organisms): # This animal class is parent class.

    def eat(self):
        print("This animal is eating.")

class Dog(Animal):

    def bark(self):   # This dog class is child class.
        print("This dog is barking.")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
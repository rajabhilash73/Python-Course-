"""
Method Overriding
"""
class Animal:     # Parent class
    def eat(self):
        print("This animal is eating.")

class Rabbit(Animal):   # Child class
    def eat(self):
        print("This rabbit is eating a carrot.")   #Overridden the parent class

rabbit = Rabbit()
rabbit.eat()
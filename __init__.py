"""
___init___ method is a special method (or also called a constructor) that is automatically
called when a new class is created. It is used to initialize object's attributes.
- Used to construct or create a new object.
Using ___init___ it makes code cleaner, more structured and objects attributes
are guaranteed to be initialized when an object is created.
"""
class Person:
    def __init__(self, name, age):
        self.name = "Abhilash"
        self.age = 25
        
P1 = Person("Abhilash", 25)    
print(P1.name) 
print(P1.age)   
        
"""
Class Variables = Class variables are variables that are shared among all instances of a class.
They are defined inside the class variables. But outside the constructor.

Instance Variables = A instance variables is declared inside the constructor. 
And they can be give unique values.
"""
from Car import Car

car_1 = Car("Medcedes", "Benz", 2025, "Black")
car_2 = Car("Ford", "Mustang", 2025, "Red")
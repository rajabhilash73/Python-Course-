"""
Python Object - Oriented Programming

Object - An object is an instance of a class.
Class - A class is an instance or a blueprint of an object.
"""

from Car import Car

car_1 = Car("Medcedes", "Benz", 2025, "Black")
car_2 = Car("Ford", "Mustang", 2025, "Red")
# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)

car_1.drive()
car_1.stop()

Car.wheels = 2

print(car_1.wheels)
print(car_2.wheels)
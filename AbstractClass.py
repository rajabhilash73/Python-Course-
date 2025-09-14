"""
Abstract Classes = Abstract classes prevents a user from creating an object of that class.
+ compels a user to override abstract methods in a child class.

A class which contains one or more abstract methods is called abstract class.
A method that has a declaration but does not have an implementation is called abstract method.
"""
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car.")
    def drive(self):
        print("You drive the car.")
    def brake(self):
        print("You brake the car.")
    def stop(self):
        print("You stop the car.")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def drive(self):
        print("You ride the motorcycle.")
    def brake(self):
        print("You brake the motorcycle.")
    def stop(self):
        print("You stop the motorcycle")

# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()
#vehicle.drive()
car.drive()
car.brake()
car.stop()

#vehicle.drive()
motorcycle.drive()
motorcycle.brake()
motorcycle.stop()


"""
Method Chaining = Method chaining is used to call multiple methods sequentially, and each call performs an action
on the same objects and returns self.
"""

class Car:
    def turn_on(self):
        print("You turn ion the car's engine.")
        return self

    def drive(self):
        print("You drive the car.")
        return self

    def brake(self):
        print("You brake the car.")
        return self

    def turn_off(self):
        print("You turn off the car engine.")
        return self

car = Car()
car.turn_on().drive().brake().turn_off()
# car.drive()
# car.brake()
# car.turn_off()
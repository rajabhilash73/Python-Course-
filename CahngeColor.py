class Car:
    color = None

class Bike:
    color = None

def change_color(vehicle, color):
    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()
car_4 = Car()

bike_1 = Bike()
bike_2 = Bike()

change_color(car_1, "Black")
change_color(car_2, "Blue")
change_color(car_3, "White")
change_color(car_4, "Red")
change_color(bike_1, "Gray")
change_color(bike_2, "Green")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(car_4.color)
print(bike_1.color)
print(bike_2.color)
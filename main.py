class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int, fuel_type: str) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        self.fuel_type = fuel_type
        
    def drive(self, distance: float) -> None:
        print(f"The {self.brand} and model {self.model} is driving for {distance} km, at the speed of {self.speed} km/h.")   
        
Volvo: Car = Car("Volvo", "XC780", 2025, 120, "Diesel")
BMW: Car = Car("BMW", "ATF8070", 2024, 150, "Electric")

print(Volvo.brand)
print(Volvo.model)
print(Volvo.drive(200))
print(Volvo.speed)

print(BMW.brand)
print(BMW.model)
print(BMW.drive(300))
print(BMW.speed)

# balance = 2200

# while True:
#     try:
#         num = float(input("Enter the amount to deposit : "))
#         break
#     except ValueError:
#         print("Invalid input. Please enter a value input.")

# balance += num
# print(f"Your new balance is {balance}")

balance = 2200

while True:
    try:
        num = float(input("Enter the amount to deposit: "))
        break   # exit loop once valid input is entered
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

balance += num
print(f"Your new balance is {balance}")
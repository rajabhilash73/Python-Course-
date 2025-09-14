"""
Self is the instance of the class. 
"""
class Player:
    def __init__ (self, name: str, level: str, health: int)-> None:
        self.name = name
        self.level = level
        self.health = health
        
    def introduce(self):
        print(f"Hello, I am {self.name}. I am a {self.level} level player, and my health is {self.health}.")
        
    def play(self):
        self.level += 1
        self.health =+ 10
        print(f"{self.name} is now level {self.level} and health is {self.health}.") 
        
player = Player("Abhilash", 61, 40)
player.introduce()
player.play()
print(f"The player name is {player.name}.")
print(f"The player level is {player.level}.")

player2 = Player("Bob", 45, 35)
player.introduce()
player.play()
print(f"The player name is {player2.name}.")
print(f"The player level is {player2.level}.")


class Bike:
    def __init__(self, brand: str, model: str, year: int, speed: int, mileage: int, turned_on : bool, turned_off: bool) -> None:  # Self is the instance of the class
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        self.mileage = mileage
        self.turned_on = turned_on
        self.turned_off = turned_off
        
    def ride(self, distance: float):
        print(f"The {self.brand} and model {self.model} is riding by abhilash for {distance} km, at the speed of {self.speed} km/h.")  
        print("The mileage of the bike is ", self.mileage, "km/litre.")  
        
    def turn_on(self) -> None:
        if self.turned_on:
            print(f"The bike {self.brand}is alreday turned on.")
        else:
            self.turned_on = True
            print("The bike is now turned on.")
            
    def turn_off(self) -> None:
        if self.turned_off:
            print(f"The bike {self.brand} bike is alreday turned off.")
        else:
            self.turned_off = True
            print("The bike is now turned off.")
                    
            
        
Yamaha = Bike("Yamaha", "Classic 350", 2025, 120, 75, True, False)        
print(Yamaha.brand)
print(Yamaha.model)
print(Yamaha.ride(200)) 
print(Yamaha.turn_on())  
print(Yamaha.turn_off())     
        
Royal_Enfield  = bike = Bike("Royal Enfield", "Bullet", 2025, 220, 35, True, False)        
print(Royal_Enfield.brand)
print(Royal_Enfield.model)
print(Royal_Enfield.ride(140))
print(Royal_Enfield.turn_on())   
print(Royal_Enfield.turn_off())     
        
class Car:\
    
    wheels = 4
    
    def __init__(self, make, model, year, color):
        self.make = make  # Instance variable
        self.model = model # Instance variable
        self.year = year   # Instance variable
        self.color = color # Instance variable
    
    def drive(self):
        print("This" + " " + self.model+ " " + " car is driving.")
        
    def stop(self):
        print("This" + " " + self.model+  " " + " car is stopped.")    
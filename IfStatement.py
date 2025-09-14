"""
if statement = A block of code that will execute if it's condition is True.
"""
age = int(input("How old are you? :"))

if age >= 18:
    print("You are an adult!")

elif age == 100:
    print("You are a centuriuan!")
    
elif age < 0:
    print("You are not born yet!")

else:
    print("You are a child!")
    


check = True
if check == False:
    print("It is false")
else:
    print("It is actually equal to true")
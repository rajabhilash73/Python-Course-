"""
Logical Operator (and, or, not) = Used to check if two or more conditional statements is True.
"""
temp = int(input("What is the temprature outside? : "))

# and logical operator
# if temp >= 0 and temp <= 30:
#     print("The temprature is good today!")
#     print("Go outside and have fun!")
  
# # or loigical operator    
# elif temp < 0 or temp > 30:  # So the Or logical operator if one condition is true then the entire statement is true.
#     print("the temprature is bad today!")
#     print("Stay inside!")
    
# and logical operator - it generally lips the condition if condition is true then it flips into the false and if false then it turns into the true.
if not(temp >= 0 and temp <= 30):
    print("The temprature is good today!")
    print("Go outside and have fun!")
    
elif not(temp < 0 or temp > 30):  # So the Or logical operator if one condition is true then the entire statement is true.
    print("the temprature is bad today!")
    print("Stay inside!")
          
"""
Input = A function that prompts the users to enter data and returns the entered data as a string.
"""
from mistune import markdown
from webcolors import names

# name = input("What is your name?: ")
# age = int(input("What is your age?: "))
# age = age + 1
# print(f"Hello {name}")
# print(f"Happy birthday {name} ")
# print(f"You are {age} years old.")
#

"""
Exercise - 1
Calculate the area of rectangle.
"""
# length = float(input("Enter the length : "))
# width = float(input("Enter the width : "))
#
# area = length * width
# print(f"The area of rectangle is: {area}cm")

"""
Exercise - 2
Shopping cart program
"""
item = input("Enter the item you want to purchase : ")
price = float(input("Enter the price of the product : "))
quantity = int(input("Enter the number of item you want : "))
total = price * quantity
print(f"The total price is : {total}")


val = input("Enter some value : ")
print(type(val), val)

name = input("Enter your name : ")
age = int(input("Enter your age : "))
marks = float(input("Enter your marks : "))

print("Welcome ", name)
print("Age : ", age)
print("Marks : ", marks)
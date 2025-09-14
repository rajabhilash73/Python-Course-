"""
Variables = A variable for a value (string, integer, float, boolean, None) This is primary data types in python.
Int - Integer data type can store value in "positive, negative and 0 form"
Str - String data type can store value in alphabetical format. Ex- "Abhilash is a python developer."
Float - Float data type can store value in decimal form. Ex - 24.99, 120,00"
Boolean - Boolean value store data in True Or False form.
None - It is a data type where we cannot store any value. Ex - a = None.
"""

First_name = "Abhilash Raj"
print(f"Hello, {First_name}")
Age = 24
print(f"I am  {Age} years old.")

"""
String Data Type: String which is store series of character
"""
first_name = "Abhilash"
last_name = "Raj"
print(type(first_name))
print("Hello" + " " + first_name + " " + last_name)

"""
Int Data Type" Int which is store whole integer
"""
age = 23
age += 1
print("Your age is: " + str(age))

"""
Float Data Type: Floating point number is decimal number.
"""
height = 250.5
print(type(height))
print("My height is : " + str(height) + "cm")

"""
Boolean Data Type: Stores True or False, and it is very useful with if statement.

"""
human = True
print(type(human))
print("Are you a human:" + str(human))

is_student = True
# print(f"Are you a student?:{is_student}")
if is_student:
    print("You are a student.")

else:
    print("You are not a student.")

for_sale = True
if for_sale:
    print("The item is for sale.")
else:
    print("The item is not for sale.")

is_online = True
if is_online:
    print("You are online.")
else:
    print("You are offline.")

name = "Abhilash"
age = 23
price = 25.99
old = False
a = None

print(type(name))  # String -- Alphabet value
print(type(age))   # Int    -- Numeric value
print(type(price)) # Float  -- Decimal value
print(type(old))   # Boolean -- True/False
print(type(a))     # None --    None value

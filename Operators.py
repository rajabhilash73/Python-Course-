"""
Operators in python - An operators is a symbol that performs a certain operation between operands.

1. Arithmetic Operators - (+, -, /, %, **)

2. Relational comparison operators-  Always return boolean value True or False. (==, != , >, <, >=, <=)

3. Assignment operators - (==, +=, -=, *=, /=, %=, **=)

4. Logical operators - ( and, or, not)
"""

# Arithmetic Operators
a = 10
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # Remainder
print(a**b) # a^b

# Relational Operators
a = 100
b = 50
print(a == b) # Return False - "==  Equal to"
print(a != b) # Return True  - "!= Not equal to"
print(a >= b) # Return True  - ">= Greater than equal to"
print(a <= b) # Return False - "<= Less than equal to"
print(a > b)  # Return True  - ">  Greater than"
print(a < b)  # Return False - "< Less than"

# Assignment operators
# =+
num = 10
# num = num + 10
num += 10
print("num : ", num)

#-=
num = 20
# num = num - 10
num -= 10
print("num : ", num)

# *=
num = 20
# num = num * 10
num *= 10
print("num : ", num)

# /=
num = 20
# num = num / 2
num /= 2
print("num : ", num)

# %=
num = 20
# num = num % 2
num%=2
print("num : ", num)

# **=
num = 20
# num = num ** 2
num **= 2
print("num : ", num)

# Logical operators
# not
a = 100
b = 60
print(not False)
print(not (a>b))

# and
# The and operator will return true when both the value is true, otherwise it will return false.
val1 = True
val2 = True
print("And operator : ", val1 and val2)

# Or operator
# The or operator return true when one value and any value is true then or operator will return true, otherwise it will return false.
val3 = False
val4 = True
print("Or operator : ", (a == b) or (a > b))



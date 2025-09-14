"""
Type Casting = Type casting is the process of converting a variable from one data type into another data type.
"""
name = "Abhilash Raj"
age = 24
CGP = 8.8
is_student = True
print(type(name))
print(type(age))
print(type(CGP))
print(type(is_student))

age = str(age) # Explicit type casting
age += "1"
print(age)

x = 1 #int
y = 2.0 # float
z = "3" #str

x = str(x)
y = str(y)
z = str(z)

print("X is " + str(x))
print("Y is " + str(y))
print(z*3)


num_str = "123"
num_int = int(num_str)
print(type(num_int)) # Output: <class 'int'>

a =float("2")
b = 4.24
print(type(a))
print(a + b)

a = int("2")
b = 4.24
print(type(a))
print(a + b)
"""
Variable Scope = The region that variable is recognised.
A variable is only available from inside the region of its created.
If a variable is created inside a function, it is not available outside the function.
L - Local
E - Enclosing
G - Global
B - Built-in
"""
name = "Abhilash" # golbal variable : it is available inside and outside the function
def display_name():
    name = "Raj" # local variable : because it is created inside a variable.
    print(name)
    
print(name) 
display_name()   
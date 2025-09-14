"""
Args = Args is a parameter that will pack all the arguments into the tuple useful so that
a function can accept a varying number of arguments.
"""
"""
Before we apply the *args parameter to the function the function gives only selective output.
"""
# Ex-
def add(num1, num2):
    return num1 + num2
print(add(40, 60))

"""
After we apply *args parameter to the function we can add multiple numbers and receive the required output.
"""

def add_num(*args):   # The *args syntax allows the function to accept a variable number of arguments. 
                       # All the arguments passed to the function will be accessible as a tuple named args.
    sum = 0  #This initializes a variable sum with the value 0.
    for i in args:    #This is a for loop that iterates over each element in the args tuple.
        sum += i
    return sum
    
print(add_num(200, 400, 500))

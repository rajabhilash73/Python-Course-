"""
Keyword Arguments = Arguments preceded by an identifier when we passed them to a function.
The order of an argument doesn't matter, unlike positional arguments.
Python knows the names of the arguments that our functions recieves.
"""
def hello(first, middle, last):
    print("Hello" + " " + first + " " + last)
    print("Nice to meet you buddy!")
    
hello(first = "Abhilash", middle = "Raj", last = "Choudhary")    
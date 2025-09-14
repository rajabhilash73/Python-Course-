"""
**kwargs = **kwargs is a parameter that will pack all the arguments into the dictionary.
Useful so that a function can accept varying number of keyword arguments.
**kwargs stands for keyword arguments.
"""
def hello(**kwargs):
    #print("Hello" + " " + kwargs["first_name"] + " " + kwargs["last_name"])
    print("Hello", end = " ")
    for key, value in kwargs.items():
        print(value, end = " ")
    
hello(first_name = "Abhilash",  middle_name = "Raj", last_name =  "Choudhary")    

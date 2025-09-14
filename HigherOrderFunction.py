"""
Higher order function = A function that either:
1. Accepts the function as an argument or
2. Returns a function
(In python function is also treated as an object.)
"""

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = (divisor(2))
print(divide(10))

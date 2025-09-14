"""
Recursion - Recursion is a programming technique where functions call itself directly or indirectly
to solve the problem.

-- A recursive function breaks the big problems into smaller subproblems of the same type,
until it reaches a stopping point called base class.
"""
# Fibonacci series using recursion

def fibonacci(n):
    if n <= 1:  # base case
        return n
    else:  # recursive case
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))

# factorial using recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# Sum of natural numbers using recursion

def sum_natural_numbers(n):
    if n == 0: # base case
        return 0
    else:
        return n + sum_natural_numbers(n-1)
print(sum_natural_numbers(5))
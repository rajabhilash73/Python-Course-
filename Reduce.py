"""
reduce() = apply a function to an iterable and reduce it to a single cumulative value.
Performs function on the first two elements and repeats the process until 1 value remains.
reduce(function, iterable)
"""
import functools
Letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y : x + y , Letters)
print(word)

Factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, Factorial)
print(result)


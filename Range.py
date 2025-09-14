"""
Range = Range is a functions that returns sequence of a numbers, starting from zero(0) by default,
and increments by 1 by default, and stops before the specified number.
"""
seq = range(5)
for x in seq:
    print(x)

# Print even numbers
nums = range(10)
for i in nums:
    if i % 2 == 0:
        print(i)

# Print odd numbers
nums = range(20)
for i in nums:
    if i % 2 != 0:
        print(i)

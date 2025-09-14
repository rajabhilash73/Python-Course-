"""
Index Operator [] = Index operator gives access to a sequence's elements(str, list, tuples)
"""
# a = 270
# b = 270
# print(a is b)  # is operator is identity check operator not equality check opeator

# a = 27
# b = 27
# print(a is b)
    
    
#  print(2 ** 3 ** 2) 

# numbers = [1, 3, 4, 8]    # [1, 6, 2, 8]
# numbers[1:3] = [6, 2]
# print(numbers)

# def weired_function(x = []):
#     x.append(1)
#     return x

# print(weired_function())
# print(weired_function())
# print(weired_function())

# def fixed_function(x=None):
#     if x is None:
#         x = []
#     x.append(1)
#     return x

# a = [1, 2, 3, 4]
# print(a[4:])

# a = [1, 2, 3, 4]
# b = a
# b.append(5)
# print(a)

name = "abhilash raj!"
# if(name[0].capitalize()):
#     name = name.islower()
 
first_name = name[:8].upper() 
last_name = name[9:].upper()
last_element = name[-1]
print(first_name)
print(last_name)
print(last_element)

# String indexing
"""
In index form we can only access the characters not modify them.
"""
str = "Abhilash Raj"
ch = str[1]
print(ch)
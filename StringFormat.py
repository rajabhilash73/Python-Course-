"""
String Format = Optional methods that gives users more control when displaying items.
"""
# animal = "cow"
# item = "moon"
# print("The" + " " + animal + " " + "jumped over the" + " " + item)


# How to write in string format method

# print("The {} jumped over the {}".format("cow", "moon")) # value 
# # print("The {1} jumped over the {0}".format(animal, item ))   # Positional arguments
# print("The {animal} jumped over the {item}".format(animal = "cow" , item = "moon" )) #keyword Arguments

# text = "The {} jumped over the {}."
# print(text.format("cow", "moon"))


# name = "Abhilash"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))


number = 1000
# print("The value of pi is {:.2f}".format(number))
print("The number is {:,}".format(number)) # Comma seprated value
print("The number is {:b}".format(number)) # Binary case
print("The number is {:o}".format(number)) # Octate case 
print("The number is {:X}".format(number)) # Hexadecimal case
print("The number is {:E}".format(number))  # Scientific notation
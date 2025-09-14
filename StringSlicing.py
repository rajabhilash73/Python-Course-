"""
Slicing = Create a substring by ectracting elements from another string.

indexing [] or slice ()

[start:stop:step]
"""
#
# name = "Abhilash Raj"
# print(name[9:12])

#first_name = name[0]# It is a starting index of string slicing
 
#print(first_name)

# first_name = name[:4] # In string slicing the first index is inclusive and the last index is exclusive [0:4]
# last_name = name[4:]     [4:end]
# funky_name = name[::2]   [0:end:2]
# reversed_name = name[::-1] [0:end:-1]
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

# website1 = "http://google.com"
# website2 = "http://facebook.com"
# slice = slice(7,-4)
# print(website1[slice])


# print(website2[slice])
#
# name = "Abhilash Raj"
# print(name[:8])
# print(name[9:])

# .endswith() - Return True if the string ends with specified suffix, otherwise, it will return false.
str = "I am Abhilash Raj. And i am a Python Developer, and i am working in google as Python Developer."
print(str.endswith("er."))

# .capitalize() - It returns capitalize version of string.
str = "i am Abhilash Raj. And i am a Python Developer, and i am working in google as Python Developer."
str = (str.capitalize())
print(str)

# .replace() - Return with copy with all occurences of substrings old replaced by new.
str = "I am Abhilash Raj. And i am a Python Developer, and i am working in google as Python Developer."
print(str.replace("Raj", "Choudhary"))

# .find() - Returns first index of first occurence.
str = "I am Abhilash Raj. And i am a Python Developer, and i am working in google as Python Developer."
print(str.find("Developer"))

# .count() - It will counts the occurence of the substring.
str = "I am Abhilash Raj. And i am a Python Developer , and i am working in google as Python Developer."
print(str.count("am"))

# .join - It can concatenate any number of strings.
str = "I am Abhilash Raj. And i am a Python Developer , and i am working in google as Python Developer."
result = " ".join(str)
print(result)


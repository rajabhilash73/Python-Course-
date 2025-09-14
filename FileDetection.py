import os

path = "C:\\Users\\Abhilash\\OneDrive\\Desktop\\folder"

if os.path.exists(path):
    print("That location exists!")
    
    if os.path.isfile(path):
        print("That is a folder!")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")


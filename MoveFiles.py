import os
source = "folder"
destination = "C:\\Users\\Abhilash\\OneDrive\\Desktop\\folder"

try:
    if os.path.exists(destination):
        print("File already exists")
    else:
        os.replace(source, destination) 
        print(source + " Was moved")
except FileNotFoundError:
    print(source + "Was not found")
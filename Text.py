# try:
    
#     with open("Text.tx")as file:
#         print(file.read())
    
# except FileNotFoundError:
#     print("That file doesn't exists!" )
    
  
# text = "I Love you my wife nishi.\nThis is my feelings to you,\nAnd one day i will express my feelings towards you infront of the world.\n"  
# with open("Test.txt", "w") as file:
#     file.write(text)    

    
# text = "Abhilash Loves Nishi"  
# with open("Test.txt", "a") as file:
#     file.write(text)  


"""
copyfile() - copies contents of a file.
copy() - copyfile() + permission mode + destination can be a directory
copy2() - copy() + copies metadeta(files creation and modification times.)
"""
import shutil
shutil.copyfile("Test.txt", "C:\\Users\\Abhilash\\OneDrive\\Desktop\\copy.txt") # src, dst

import shutil
shutil.copy("Test.txt", "C:\\Users\\Abhilash\\OneDrive\\Desktop\\copy.txt")

import shutil
shutil.copy2("Test.txt", "C:\\Users\\Abhilash\\OneDrive\\Desktop\\copy.txt")
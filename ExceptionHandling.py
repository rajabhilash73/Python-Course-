"""
Exception Handling = An exception is a events detected during execution that interupt the flow of a 
program.
"""
try:     # Tells python to "Try" running the code inside the  block
    numerator = int(input("Enter a number to divide : "))
    denominator = int(input("Enter a number to divided by : "))
    result = numerator / denominator
    # print(result)   # If any error/exception will rise in this block, it will jump to the except block.
    
except ZeroDivisionError:
    print("You can't divide by zero! idiot!")
    
except ValueError:
    print("Invalid input. Please try again with a number.")
    
except Exception as e:
    print(e)
    
except Exception:   # Catches all the exception using the base calss exception.
    print("Something went wrong ):")  # If any error occurs in the try block(eg. invalid input, division by zero) python skips the try code and runs the except block.  
    
else:
    print(result)
    
finally:
    print("This will always execute")  # This will used in file handling.
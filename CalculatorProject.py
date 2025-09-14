 # Calculator project

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Take input from the user

print("Select operations.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice(1/2/3/4): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "4":
    if num2 != 0:
        print("Result: ", divide(num1, num2))
    else:
        print("Error: Division by zero not allowed.")

else:
    print("Invalid input.\nTry again.")


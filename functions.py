# Simple Calculator Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero")
    else:
        return a / b


while True:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /)")

    if operation == '+':
        print("Result:", add(num1, num2))
    elif operation == '-':
        print("Result:", subtract(num1, num2))
    elif operation == '*':
        print("Result:", multiply(num1, num2))
    elif operation == '/':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation. Please try again.")

    choice = input("Do you want to continue? (y/n): ").lower() 
    if choice == 'n': print("Goodbye!")
    break

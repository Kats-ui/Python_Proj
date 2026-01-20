#Updated simple calculator program with functions for each operation

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    while True:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        
        if operation == '+':
            result = add(num1, num2)
            print(result)
        elif operation == '-':
            result = subtract(num1, num2)
            print(result)
        elif operation == '*':
            result = multiply(num1, num2)
            print(result)
        elif operation == '/':
            result = divide(num1, num2)
            print(result)
        else:
            print("Invalid operation!")

        choice = input("Do you want to perform another calculation? (yes/No): ")
        if choice.lower() != 'yes':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Starting a new calculation...")

calculator()

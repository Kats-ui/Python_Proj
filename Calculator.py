# Mini classic calculator
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
total = 0
operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    total = num1 + num2
    print("The result is:", total)
elif operation == "-":
    total = num1 - num2
    print("The result is:", total)
elif operation == "*":
    total = num1 * num2
    print("The result is:", total)
elif operation == "/":
    total = num1 / num2
    print("The result is:", total)
else:
    print("Invalid operation")



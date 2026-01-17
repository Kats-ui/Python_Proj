# Mini classic calculator
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = 0
operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    num3 = num1 + num2
    print("The result is:", num3)
elif operation == "-":
    num3 = num1 - num2
    print("The result is:", num3)
elif operation == "*":
    num3 = num1 * num2
    print("The result is:", num3)
elif operation == "/":
    num3 = num1 / num2
    print("The result is:", num3)
else:
    print("Invalid operation")



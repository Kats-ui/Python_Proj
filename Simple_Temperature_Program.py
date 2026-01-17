#Temperature Conversion program
print("-------------------------------")
print("Temperature Conversion Program")
print("-------------------------------")

print("Select the conversion you want to perform: C for Celsius to Fahrenheit and F for Fahrenheit to Celsius")
temp_conversion = input("Enter your choice (C/F): ")
print("-------------------------------")
temp_amount = float(input("Enter the temperature you want to convert: "))
if temp_conversion.upper() == "C":
    temp_converted = (temp_amount * 9/5) + 32
    print(f"The converted temperature is: {temp_converted} °F")
elif temp_conversion.upper() == "F":
    temp_converted = (temp_amount - 32) * 5/9
    print(f"The converted temperature is: {temp_converted} °C")
else:
    print("Invalid choice")



import calculator

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":    
    result = calculator.add(a, b)
elif operation == "-":
    result = calculator.subtract(a, b)
elif operation == "*":
    result = calculator.multiply(a, b)
elif operation == "/":
    result = calculator.divide(a, b)
else:
    result = "Invalid operation"

print(result)
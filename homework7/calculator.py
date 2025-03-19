import math_tools # type: ignore

a = float(input("Enter the first number: "))
b = float(input("Enter the first number: "))
operation = input("Which operation: ")

if operation == "add":
    print(math_tools.add(a,b))
if operation == "subtract":
    print(math_tools.subtract(a,b))  
if operation == "multiply":
    print(math_tools.multiply(a,b))
if operation == "divide":
    print(math_tools.divide(a,b))
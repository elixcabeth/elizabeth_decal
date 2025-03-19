def add(a, b):
    return a + b
# returns the sum of a and b

def subtract(a , b):
    return a - b
# returns the difference of a and b

def multiply(a , b):
    return a * b
# returns the product of a and b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b
# returns the quotient of a and b and accounts for division by zero
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    num1 = float(input("Type first number: "))
    operator = input("Choose an operator (+, -, *, /): ")
    num2 = float(input("Type second number: "))
    
    if operator == '+':
        result = add(num1, num2)
    
    elif operator == '-':
        result = subtract(num1, num2)
    
    elif operator == '*':
        result = multiply(num1, num2)
    
    elif operator == '/':
        result = divide(num1, num2)
        
    else:
        print("Invalid an operator.")
        return main()
        
    print("Result: ",result)

main()

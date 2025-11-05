print("=== Simple CLI Calculator ===")
a = float(input("Enter first number: "))
op = input("Enter operation (+ - * /): ")
b = float(input("Enter second number: "))

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")


# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def main():
    print("🧮 Simple Calculator (Python CLI)")
    print("Select operation: + - * /")
    
    while True:
        op = input("Enter operation (+, -, *, / or 'q' to quit): ").strip()
        if op == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if op not in ('+', '-', '*', '/'):
            print("Invalid operator. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)

        print(f"Result: {result}\n")

if __name__ == "__main__":
    main()

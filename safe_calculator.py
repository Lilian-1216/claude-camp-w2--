def get_number(prompt):
    """Get a number from user. Return None if user types 'quit'."""
    while True:
        value = input(prompt).strip()
        if value.lower() == "quit":
            return None
        try:
            return float(value)
        except ValueError:
            print("Invalid number. Please try again (or type 'quit' to exit).")

def get_operator():
    """Get a valid operator from user. Return None if user types 'quit'."""
    while True:
        op = input("Operator (+, -, *, /): ").strip()
        if op.lower() == "quit":
            return None
        if op in ("+", "-", "*", "/"):
            return op
        print("Invalid operator. Use +, -, *, / (or type 'quit' to exit).")

print("Safe Calculator. Type 'quit' anytime to exit.\n")

while True:
    a = get_number("First number: ")
    if a is None: break

    op = get_operator()
    if op is None: break

    b = get_number("Second number: ")
    if b is None: break

    try:
        if   op == "+": result = a + b
        elif op == "-": result = a - b
        elif op == "*": result = a * b
        elif op == "/": result = a / b
        print(f"Result: {a} {op} {b} = {result}\n")
    except ZeroDivisionError:
        print("Error: cannot divide by zero.\n")

print("Thanks for using the Safe Calculator.Goodbye!")
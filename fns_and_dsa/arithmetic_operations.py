# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation.
    operation must be one of: 'add', 'subtract', 'multiply', 'divide'.
    Returns a float result for valid operations, or a message for errors.
    Division by zero returns the string: "Cannot divide by zero"
    """
    op = str(operation).strip().lower()
    a = float(num1)
    b = float(num2)

    if op == "add":
        return a + b
    if op == "subtract":
        return a - b
    if op == "multiply":
        return a * b
    if op == "divide":
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    return "Invalid operation"

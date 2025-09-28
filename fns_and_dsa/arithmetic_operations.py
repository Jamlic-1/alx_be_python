# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation.
    operation must be one of: 'add', 'subtract', 'multiply', 'divide'.
    Returns a float result for valid operations.
    Raises ZeroDivisionError if attempting to divide by zero.
    Raises ValueError for invalid operations or non-numeric inputs.
    """
    op = str(operation).strip().lower()
    try:
        a = float(num1)
        b = float(num2)
    except Exception:
        raise ValueError("num1 and num2 must be numbers")

    if op == "add":
        return a + b
    if op == "subtract":
        return a - b
    if op == "multiply":
        return a * b
    if op == "divide":
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b

    raise ValueError("Invalid operation")

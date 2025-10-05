# === robust_division_calculator.py ===
except (ValueError, TypeError):
return "Error: Please enter numeric values only."


try:
result = num / den
except ZeroDivisionError:
return "Error: Cannot divide by zero."


return f"The result of the division is {result}"




# === main_division.py (CLI for safe_divide) ===
import sys
from robust_division_calculator import safe_divide




def main():
if len(sys.argv) != 3:
print("Usage: python main_division.py <numerator> <denominator>")
sys.exit(1)


numerator = sys.argv[1]
denominator = sys.argv[2]


result = safe_divide(numerator, denominator)
print(result)




if __name__ == "__main__":
main()

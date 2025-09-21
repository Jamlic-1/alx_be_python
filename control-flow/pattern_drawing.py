# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # move to the next line
    row += 1

# Data Science Fundamentals Assessment
# Part 1: Python Basics

print("DATA SCIENCE FUNDAMENTALS ASSESSMENT")
print("Python Basics")
print("-" * 40)

# Variables
name = "Student"
age = 20
marks = 85.5

print("Name:", name)
print("Age:", age)
print("Marks:", marks)

# Arithmetic operations
a = 10
b = 5

print("\nArithmetic Operations")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# Conditional statement
if marks >= 40:
    print("\nResult: Pass")
else:
    print("\nResult: Fail")

# Loop
print("\nNumbers from 1 to 5:")

for i in range(1, 6):
    print(i)

# Function
def calculate_square(number):
    return number * number

print("\nSquare of 5:", calculate_square(5))
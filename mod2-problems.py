# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."

print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.

# 1st is to handle with first 2 numbers
def perform_operations():
    # Get user input for two numbers
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))

    # show the outcome of equation
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    # Check if 0 is never in division
    if num2 != 0:
        division = num1 / num2
    else:
        division = "undefined(cannot divide by zero)"

    # Display the results
    print(f"\nResults:")
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} * {num2} = {multiplication}")
    print(f"{num1} / {num2} = {division}")

# FINAL OUTCOME
perform_operations()

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)

import math

# Get the side lengths from the user
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
# Calculate the semi-perimeter
s = (a + b + c) / 2
# Calculate the area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
# Output the area
print(f"The area of the triangle is: {area:.2f}")

#4 Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).

import math
# get five numbers from the user
numbers=[]
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate the total (sum)
total = sum(numbers)

# Calculate the average
average = total / len(numbers)

# Calculate the minimum and maximum
minimum = min(numbers)
maximum = max(numbers)

# Calculate the range
range_value = maximum - minimum

# Calculate the standard deviation
variance = sum((x - average) ** 2 for x in numbers) / len(numbers)
standard_deviation = math.sqrt(variance)

# output of all equations
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Range: {range_value}")
print(f"Standard Deviation: {standard_deviation:.2f}")

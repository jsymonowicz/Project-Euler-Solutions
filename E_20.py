"""
Problem 20
Factorial Digit Sum
Find the sum of the digits in the number 100!
Solution: 648
"""
# Import module which can calculate factorial
import math

# Define number to investigate
chosen_numer = 100
# Calculate factorial of the chosen number
factorial_num = math.factorial(chosen_numer)
# Initalize summation of digits in the factorial output
sum_factorial = 0

# Sum digits in the factorial output
for i in str(factorial_num):
    sum_factorial += int(i)

# Print out the solution
print(sum_factorial)
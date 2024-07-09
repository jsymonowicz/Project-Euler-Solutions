# -*- coding: utf-8 -*-
"""
The difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""

import time

start_time = time.time()

sum_of_squares = 0
num_sum = 0
for i in range (1, 101):
    num_sum += i
    sum_of_squares += i**2
square_of_sum = num_sum**2
difference = square_of_sum - sum_of_squares
print(difference)
end_time = time.time()
total_time = end_time - start_time
print(total_time)
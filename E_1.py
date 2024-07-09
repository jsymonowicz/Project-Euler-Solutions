"""
Problem 1
Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6, 9. The sum of these multiples is 23. Find the sum of all the 
multiples of 3 or 5 below 1000.

Answer: 233168
"""
max_num = 1000
i = 3
sum_3_5 = 0

while i < max_num:
    if i % 3 == 0:
        sum_3_5 += i
    elif i % 5 == 0:
        sum_3_5 += i
    i += 1
    
print(f"The sum of multiples of 3 or 5 below 1000 is {sum_3_5}.")
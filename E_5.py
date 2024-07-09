# -*- coding: utf-8 -*-
"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""
import time

start_time = time.time()

num = 0
i = 1

dividers = [11, 12, 13, 14, 15, 16, 17, 18, 19]
length = len(dividers)
while i > 0:
    i = length
    num += 20
    for divs in dividers:
        if num % divs == 0:
            i -= 1
        else:
            break
print(num)
end_time = time.time()
total_time = end_time - start_time
print(total_time)
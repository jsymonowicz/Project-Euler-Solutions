# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10,001 st prime number?
ANSWER: 104743
"""
import time

start_time = time.time()
# Prime number generator
def prime_numbers(nth):
    prime_nums = [2]
    num = 1
    while len(prime_nums) < nth:
        num += 2
        for j in prime_nums:
            if num % j == 0:
                break
        if j == prime_nums[-1]:
            prime_nums.append(num)
    return prime_nums

nth_num = prime_numbers(40)
print(nth_num)

end_time = time.time()
total_time = end_time - start_time
print(total_time)
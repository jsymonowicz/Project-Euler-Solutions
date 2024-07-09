# -*- coding: utf-8 -*-
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Answer: 142913828922
"""
import time
import math

start_time = time.time()

# Prime number generator
def prime_numbers(max_num):
    if max_num < 2:
        return []
    
    prime_nums = [2]
    num = 3
    while num < max_num:
        sqrt_num = math.isqrt(num)
        is_prime = True
        for j in prime_nums:
            if j > sqrt_num:
                break
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)
        num += 2
    return prime_nums

prime_nums = prime_numbers(2000000)
result = sum(prime_nums)
print(result)

end_time = time.time()
total_time = end_time - start_time
print(total_time)

'''
for 2,000,000:
142913828922
543.868236541748

for 200,000:
    1709600813
    6.708573341369629
'''
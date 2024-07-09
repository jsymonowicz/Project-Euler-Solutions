# -*- coding: utf-8 -*-
'''
Which starting number, under one million, produces the longest chain?
Once the chain starts the terms are allowed to go above one million.
'''

import time

start_time = time.time()

def collatz_length(n, memo):
    original_n = n
    length = 0
    while n != 1 and n not in memo:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    if n in memo:
        length += memo[n]
    memo[original_n] = length
    return length

max_length = 0
longest_chain_num = 0
memo = {1: 1}

for i in range(1, 999999):
    length = collatz_length(i, memo)
    if length > max_length:
        max_length = length
        longest_chain_num = i

print(max_length, longest_chain_num)


end_time = time.time()
total_time = end_time - start_time
print(total_time)
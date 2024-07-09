# -*- coding: utf-8 -*-
"""
2^15 = 32768 and sum of its digits is 3+2+7+6+8 = 26
Sum of digits of num 2^1000
"""
def pow_sum(num):
    str_num = str(num)
    sum_num = 0
    for i in str_num:
        sum_num += int(i)
    return(sum_num)

power = 1000

num = 2**power
result = pow_sum(num)
print(result)


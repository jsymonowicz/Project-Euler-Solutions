# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers
"""
def palindrome_check(number):
    num_str = str(number)
    if num_str == num_str[::-1]:
        return True
    else:
        return False

max_val = 0
for i in range (900):
    num_1 = 999-i
    for j in range (900):
        num_2 = 999-j
        product = num_1 * num_2
        if palindrome_check(product):
            if product > max_val:
                max_val = product
print(max_val)
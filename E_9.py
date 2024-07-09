# -*- coding: utf-8 -*-
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
a2+b2 = c2. There exists exactly one Pythagorean triplet for 
which a + b + c = 1000.
Find the product abc.

Answer: 31875000
"""
#find:
#a**2 + (b**2) = (1000 - b - a)**2

max_abc = 0
for b in range(1, 999):
    for a in range(1, 998):
        if a**2 + (b**2) == (1000 - b - a)**2 and b > a:
            c = 1000 - a - b
            abc = a*b*c
            print("a=", a,"b=", b, "c=", c, "abc=", abc)
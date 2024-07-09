# -*- coding: utf-8 -*-
"""
Starting in the top left corner of a 2x2  grid, and only being able to move
to the right and down, there are exactly routes to the bottom right corner.
"""

import math

def count_routes_in_grid(n):
    # Calculate the binomial coefficient (2n choose n)
    return math.factorial(2 * n) // (math.factorial(n) * math.factorial(n))

# For a 20x20 grid
n = 20
number_of_routes = count_routes_in_grid(n)
print(number_of_routes)

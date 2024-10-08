# -*- coding: utf-8 -*-
"""
Problem 18
Maximum Path Sum I

Find the maximum total from top to bottom of the triangle below

Answer: 1074
"""

triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

# Create triangle replica for storing max paths values
paths = triangle
rows = len(triangle)

# Start from second row from bottom
for i in range(rows-2, -1, -1):
    # check values in a row below it
    for j in range(len(paths[i+1])-1):
        # choose bigger of two values below cell in the starting row
        max_path = max(paths[i+1][j], paths[i+1][j+1])
        # add it to the cell above them and later move to the next row upwards
        paths[i][j] += max_path
 
# Most top value of paths contains maximum total from top to bottom of the triangle
print(paths[0][0])
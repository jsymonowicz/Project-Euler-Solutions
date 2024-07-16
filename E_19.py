"""
Problem 19
Counting Sundays
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""

# Define lengths of months
month_lengths = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30,
                 10:31, 11:30, 12:31}
    
# Calculate which years were leap years
year = 1900
leap_years = []
while year < 2000:
    year += 4
    leap_years.append(year)
    
# Start the count of Sundays falling on the 1st of the month
sundays_on_1st = 0

# 1 Jan 1900 is Monday, here we start on 1 Jan 1901
year = 1901
day = 366 # Since 1 Jan 1900

# Check days until year 2000
while year < 2000:
    for month in month_lengths:
        # Add length of the month
        day += month_lengths[month]
        # Account for length of Feburary in leap years
        if month == 2 and year in leap_years:
            day += 1
        # If the 1st day is Monday, add to summation
        if day % 7 == 1:
            sundays_on_1st += 1
    year += 1
   
print("Number of Sundays which fell on the 1st of the month during the 20th century:")
print(sundays_on_1st)
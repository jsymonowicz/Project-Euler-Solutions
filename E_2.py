"""
Problem 2
Even Fibonacci Numbers

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89,...
By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

Answer: 4613732
"""
# Enter max value in the Fibonacci sequence 
max_value = 4000000

# Initiatal values for Fibonacci sequence
Fibb_sequence = [1, 2]
i = 1

# Create Fibonacci sequence for values < 4,000,000
while True:
    new_num = Fibb_sequence[i] + Fibb_sequence[i-1]
    if new_num >= max_value:
        break
    Fibb_sequence.append(new_num)
    i += 1

# Find sum of the even-valued terms in Fibb_sequence
sum_even_terms = 0
for i in Fibb_sequence:
    if i % 2 == 0:
        sum_even_terms += i

# Print out the solution
print(sum_even_terms)
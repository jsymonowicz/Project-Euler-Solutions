"""
Problem 3
Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

Answer: 6857
"""
# Import needed libraries
import time
import math

# Check time the program takes
start_time = time.time()

# Prime number generator
def prime_numbers(max_num):
    
    #There are no prime numbers below 2
    if max_num < 2:
        return []
    
    # Define smallest prime numbers
    prime_nums = [2]
    num = 3
    
    # Calculate new prime numbers
    while num < max_num:
        sqrt_num = math.isqrt(num)
        is_prime = True
        for j in prime_nums:
            # Check until square of the divisor
            if j > sqrt_num:
                break
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)
        # Save calculation time by avoiding even numbers
        num += 2
    return prime_nums

# Define analized number
max_num = 600851475143

# It is enough to check divisors until square root of max_num
max_num_sqrt = math.isqrt(max_num)
# Generate prime numbers < than analized number
prime_nums = prime_numbers(max_num_sqrt)
# Check biggest prime number as divisors first - reverse prime number list
prime_nums.reverse()

# Break when first and thus highest prime number divisor is found
for i in prime_nums:
    if max_num % i == 0:
        break
    
# Print out highest prime number divisor
print(i)

# Calculate program run time
end_time = time.time()
total_time = end_time - start_time
print(f"Run time of the program: {total_time:.2f}s")
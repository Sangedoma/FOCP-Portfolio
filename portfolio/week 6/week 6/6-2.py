'''Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original).'''
def find_factors(n):
    if n <= 0:
        return "Input must be a positive integer."
    
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:  # Check if i is a factor of n
            factors.append(i)
    return factors

# Example usage
print(find_factors(49)) 

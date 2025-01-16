'''Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers.'''
def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(n**0.5) + 1):  # Check for divisibility up to sqrt(n)
        if n % i == 0:  # If divisible by any number, it's not prime
            return False
    return True  # If no divisors are found, it's prime

print(is_prime(29)) 
print(is_prime(81))  

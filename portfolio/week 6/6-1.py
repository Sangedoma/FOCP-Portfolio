'''Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2).
Hint: This is in many ways a trick question. Think!'''

def to_binary(n):
    if n <= 0:
        return "Input must be a positive integer."
    
    return bin(n)[2:]  

# Example usage
print(to_binary(35))

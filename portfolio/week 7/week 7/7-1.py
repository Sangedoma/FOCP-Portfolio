'''Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's'].'''

def unique_sorted_letters(message):
    # Convert the message to a set to remove duplicates, then sort the set
    unique_letters = sorted(set(message))
    return unique_letters

# Test the function
message = "cheese"
sorted_unique_letters = unique_sorted_letters(message)

print(f"Original Message: {message}")
print(f"Sorted Unique Letters: {sorted_unique_letters}")

'''Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way.'''

def encrypt_message(message):
    # Remove spaces and reverse the string
    encrypted_message = message.replace(" ", "")[::-1]
    return encrypted_message

# Test the function
message = "Today is Sunday"
encrypted_message = encrypt_message(message)
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")

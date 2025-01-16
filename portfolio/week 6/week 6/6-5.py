'''Another way to hide a message is to include the letters that make it up within
seemingly random text. The letters of the message might be every fifth characte
for example. Write and test a function that does such encryption. It should
randomly generate an interval (between 2 and 20), space the message out
accordingly, and should fill the gaps with random letters. The function should
return the encrypted message and the interval used.
For example, if the message is "send cheese", the random interval is 2, and for
clarity the random letters are not random:
send cheese
s e n d c h e e s e
sxyexynxydxy cxyhxyexyexysxye'''

import random
import string

def encrypt_message_with_interval(message):
    # Generate a random interval between 2 and 20
    interval = random.randint(2, 20)
    
    # Generate a list for the encrypted message
    encrypted_message = []
    
    # Add every 'interval' letter of the original message
    for i in range(len(message)):
        # Add the original character or a random character if we're not on the interval
        if (i % interval == 0):
            encrypted_message.append(message[i])
        else:
            encrypted_message.append(random.choice(string.ascii_lowercase))  # Add random letters
    
    # Join the list into a string
    encrypted_message_str = ''.join(encrypted_message)
    return encrypted_message_str, interval

# Test the function
message = "send cheese"
encrypted_message, interval = encrypt_message_with_interval(message)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Interval: {interval}")
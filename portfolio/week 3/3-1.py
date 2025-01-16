'''Modify your greeting program so that if the user does not enter a name (i.e. they
just press enter), the program responds "Hello, Stranger!". Otherwise it should print
a greeting with their name as before.'''

name = input("Enter your name: ")
if name: #checks if the name variable contains any value or not
    print(f"Hello, {name}! How are you today?")
else:
    print(f"Hello, Stranger!")
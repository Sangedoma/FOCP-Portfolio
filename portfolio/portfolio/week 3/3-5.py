'''Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time.'''

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:  #Loop until a valid password is chosen
    pwd_1 = input("Enter your password: ")
    pwd_2 = input("Enter your password again: ")

    #To check if either of the passwords is in the BAD_PASSWORDS list
    if pwd_1 in BAD_PASSWORDS or pwd_2 in BAD_PASSWORDS:
        print("Your chosen password is not acceptable. Please choose another one.")
    
    #To check if the password meets the length requirement which should be between 8 and 12
    elif 8 < len(pwd_1) < 12:
    
        if pwd_1 == pwd_2:
            print("Password Set")
            break  #Exit the loop if the password is valid
        else:
            print("Passwords do not match. Please try again.")
    
    else:
        print("Password must be between 8 and 12 characters long!")

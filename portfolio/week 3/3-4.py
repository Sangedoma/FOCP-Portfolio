'''Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']'''

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

pwd_1 = input("Enter your password: ")
pwd_2 = input("Enter your password again: ")

#To check if either of the password is in the BAD_PASSWORDS list
if pwd_1 in BAD_PASSWORDS or pwd_2 in BAD_PASSWORDS:
    print("Your chosen password is not acceptable. Please choose another one.")
else:
    #To check if the password meets the length requirement which should be between 8 and 12
    if 8 < len(pwd_1) < 12:
        if pwd_1 == pwd_2:
            print("Password Set")
        else:
            print("There is an error!")
    else:
        print("Password must be between 8 and 12 characters long!")





'''Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long.'''

pwd_1 = input("Enter your password: ")

#To check if the password meets the length requirement which should be between 8 and 12
if 8 < len(pwd_1) < 12:
    pwd_2 = input("Enter your password again: ")

    if pwd_1 == pwd_2:
        print("Password Set")
    else:
        print("There is an error!")
else:
    print("Password must be between 8 and 12 characters long!")


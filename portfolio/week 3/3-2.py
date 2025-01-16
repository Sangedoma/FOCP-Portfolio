'''Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error.'''

pwd_1 = input("Enter your password: ")
pwd_2 = input("Enter your password: ")

if pwd_1 == pwd_2:
    print("Password Set")
else:
    print("There is an error!")
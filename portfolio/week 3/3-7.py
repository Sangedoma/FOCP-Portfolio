users_no = int(input("Enter the number of the table you require: "))

print("Times Table Of Your Choice")

if users_no > 0:
    for n in range (0,13):
        print(f"{n} * {users_no} = {n * users_no}")





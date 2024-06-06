password = input("Please input password : ")
while len(password) < 8:
    print("Password has to be more than 8 characters.")
    password = input("Please input password : ")
print(password)
age=int(input("Please input age :"))

while age<18:
    print("You must be 18 or above to access this application.")
    break
else:
    print("Welcome to the application.")

password=str(input("Create password :"))

if len(password)<10:
    print("Password must be more than 10 characters.")
else:
    print("Password created.")
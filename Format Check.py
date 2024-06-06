while True:
    email = input("Enter your email address: ")
    if "@" not in email:  # Check if email not contain the "@" symbol
        print("Email needs an @ symbol. Please try again.")  
    else:
        break         # Exit the loop if "@" symbol is found

print("The email address you entered is:", email)

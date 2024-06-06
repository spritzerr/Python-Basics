num = input("Please enter a positive number (decimal is allowed): ")
while True:
    try:
        num = float(num)
        if num > 0:
            break
        else :
            print("Your number must be positive.")
            num = input("Please enter again ")
    except:
        print("Your entry is not a number.")
        num = input("Please enter again ")
print(num)
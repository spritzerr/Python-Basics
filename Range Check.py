num = int(input("Number : "))
while num < 1 or num > 100:
    print("Number has to be more than 1 and less than 100")
    num = int(input("Number : "))
print(num)
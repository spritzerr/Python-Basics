while True:
    age = input("Input your age: ")
    try:
        age = int(age)
        break
    except:
        print("Age must be an integer")
print(age)
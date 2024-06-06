animal_list = []

def main():
    for i in range(0,5):
        animal = str(input("Please input animal: "))
        animal_list.append(animal)
    print(animal_list)
    a = search() # The variable "a" now returns the value of "num" from the search() procedure.
    print(animal_list[a])

def search():
    num = int(input("Please input Index Number: "))
    return num # When a procedure returns a value, in this case the value "num", it becomes a function.  

main()
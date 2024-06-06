animal_list = []

def main():
    for i in range(0,5):
        animal = str(input("Please input animal: "))
        animal_list.append(animal)
    print(animal_list)
    num = int(input("Please input Index Number: "))
    search(num)

def search(j):
     print(animal_list[j])

main()

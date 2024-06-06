array=[100,50]

def main():
    InputNumber()
    Calculate()

def InputNumber():
    for i in range(0,10):
        x=int(input("Please enter a number :"))
        array.append(x)


def Calculate():
    total=sum(array)
    average=total/len(array)
    print(total)
    print(average)

main()
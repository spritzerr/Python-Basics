def main():
    marklist=[]
    for i in range(0,4):
        num = checkmark(i+1)
        marklist.append(num)
    print("Your marks are: ")
    marklist.sort(reverse=True)
        
    
    for i in marklist:
        print(i,end=" ")
    
    counter = 0
    for j in marklist:
        if j>=80:
            counter += 1
    
    print()
    print(f"The number of marks with HD is {counter}")
    print("The average of the marks is " +str(sum(marklist)/len(marklist)))
    print("The total of the lowest two marks is " +str(sum(marklist[-2:])))
    print("The total of the highest two marks is " +str(sum(marklist[:2])))

def checkmark(j):
    while True:
        num = input(f"Enter marks for unit number {j} : ")
        if len(num)==0: # Presence check
             print("No input was detected!")
             continue
        try:
            num=float(num)
            if num<0 or num>100:
                print("Your marks cannot be negative value or more than 100.")
            
            else:
                return num
        except:
            print("Your input is not a number")

main()
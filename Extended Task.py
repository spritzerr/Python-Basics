num_list = [] # establishing the list

def main():
    for i in range(0,6):
        num = validate(i+1) # "i+1" is used as a counter.
        num_list.append(num) # integrating the user inputs into the list.
    print(num_list)
    
    for s in num_list: # Printing the elements instead of the list.
        print(s, end=" ") # end is used to print the output in horizontal format.
        

def validate(t): # "t" is used as a variable to catch the "i+1" parameter.
    while True:
        try:
            num=float(input(f"{t}.Please enter a positive number (decimal is allowed): ")) # f string can be used to make the list.
            if num > 0: # Check for positive number.
                print(num)
                return num # "return" can also break an infinite loop. 
            else :
                print("Your number must be positive.") # Error message
        except:
            print("Your data entry is not a number.") # Error message

main() # Call main()

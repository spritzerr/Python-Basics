def main():
    income = validate()
    pay = calc(income)
    
    print(f"Your pre-tax income is ${income:,.2f}")
    print(f"Your tax payable is ${pay:,.2f}")
    print(f"Your after-tax income is ${income-pay:,.2f}")
    
def validate():
    income = input("Enter your pre-tax income ")
    while True: 
        try :
            income = int(income)
            if income < 0:
                income = input("Enter your pre-tax income properly ")
            else:
                return income
        except :
            income = input("Enter your pre-tax income properly ")

def calc(income):
    if income <= 10000:
        pay = 0.25*income
    
    elif income > 10000 and income <= 20000:
        pay = 2500 + (0.35*(income-10000))
    
    else:
        pay = 6000 + (0.45*(income-20000))
    
    return pay

main()
        

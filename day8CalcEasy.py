while True:
    num1=float(input("Enter the first number: "))
    operator=input("Enter the Operator(+,-,*,/): ")
    num2= float(input("Enter the second number: "))

    if operator=='+':
        print("Result: ", num1+num2)

    elif operator=='-':
        print(f'Result: {num1-num2}')

    elif operator=='*':
        print(f'Result: {num1*num2}')
        
    elif operator=='/':
        if num2 ==0:
            print("ZeroDivisionError: Cannot divide by Zero")
        else: 
            print("Result: ",num1/num2)
    else:
        print("Invalid Operation")
                
    choice=input("Do you want to exit?(y/n)").lower()
    if choice=='y':
        print("\n Thank you\nExiting.....")
        break        



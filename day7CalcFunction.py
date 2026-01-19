def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Error: Division by Zero is not allowed!"
    return a/b

def exponential(a,b):
    return a**b

def calculator():
    print("SIMPLE CALCULATOR".center(40,"="))
    while True: 
        print("\nOperations: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponential")
        print("6. Exit")
        print("-"*40)
        
        choice=input("choose an operation(1-5): ")
        
        if choice=='6':
            print("\n Thank you for using my calculator! ")
            print("Exiting----")
            break
        
        if choice not in ['1','2','3','4','5']:
            print("\n Invalid choice! Please select 1-5. ")
            continue
        
        try:
            num1=float(input("\nEnter first number: "))
            num2=float(input("\nEnter second number: "))
            
            print("\n")
            if choice=='1':
                print(f'Result: {add(num1,num2)} ')
            
            elif choice=='2':
                print(f'Result: {subtract(num1,num2)}')
           
            elif choice=='3':
                print(f'Result: {multiply(num1,num2)}')
            
            elif choice=='4':
                print(f'Result: {divide(num1,num2)}')
                
            elif choice=='5':
                print(f'Result: {exponential(num1,num2)}')
                          
            print("\n" +"="*40)
        except ValueError:
            print("\n Error: Please enter valid numbers!")


calculator()
                                        
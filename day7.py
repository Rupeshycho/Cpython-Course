#module operato 
print(f'Module operator: {15//2}') #7
print(f'Remainder operator: {5%3}') #2
print(f'Exponential operator: {5**3}') #15

print('\n')
print("Simple Calculator".center(40,"="))

#Take inputs 
num1= float(input("Enter the first  number: "))
num2=float(input("Enter the second number: "))

#choose operation 
print("Choose operation\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

print("n")
choice=int(input("Enter the choice(1/2/3/4): "))

#calculation
if choice==1:
    result=num1+num2
    print(f'Addition: {result}')
    
elif choice==2:
    result=num1-num2
    print(f'Subtraction: {result}')
elif choice==3:
    result=num1*num2
    print(f'Multiplication: {result}')
    
elif choice==4:
    if num2!=0:
        result=num1/num2
        print(f'Division: {result}')
    else:
        print("ZeroDivisionError: Division by 0 isn't allowed.")  
        
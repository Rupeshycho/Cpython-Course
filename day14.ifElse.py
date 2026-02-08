def age():
    a=int(input("Enter your age: \n "))

    if (a>18):
        print("Since, your age is: ", a)
        print("You can drive ")
    elif (a<=0 ):

        print("Invalid age")

    elif (a>=80):
        print("Since, your age is: ", a)
        print("You can drive but with caution ")    

    else:
        print(" ", a)
        print("You cannot drive. ")
        
        
def priceBudget():
    applePrice=int(input("Enter the price for apple:\nRS. "))
    budget=int(input("What's your budget?\nRs."))
    if (applePrice<=budget):
        print("Alexa, Add 1 kg of apple to the cart ") 
        
    else:
        print("Low budget, cannot buy apple. ")           

age()
priceBudget()


def elifpy():
    num=int(input("Enter a number: "))
    
    if (num>0):
        print("The number is positive. ")
        if(num==143):
            print("I love You.")
            
    elif (num<0):
        print("The number is negative. ")
        
        
    else:
        print("The number is zero. ")
        
    print(">>> The code ended Successfully. ")
        
elifpy()        

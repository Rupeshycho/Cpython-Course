#math cases  here 
import random 
import os  
print("Hello world from Rupesh Yadav.")
os.system('python --version')

def matchCase():
    x = 4
    print(f'x = {x} \nSo, case 4 runs.')
    
    match x:
        case 1:
            print("1 is a prime number ")   
            
        case 4: 
            print(" x =4 ; 4 is a even number \n")             
def days():
    day=random.choice(["sunday","monday","tuesday","wednesday","thursday","friday","saturday"])
    print(f'Randomly selected day: {day}')
    
    match day:
        case "sunday":
            print("1. Start of the Week...")
        case "saturday":
            print("7. End of the Week !!! ")    
        case _ :
            print(" Midweek Days, Work. ")    
days() 

def stages():
    print("Stages of Life".center(40,"="))
    while True:
        try:
            age=int(input("Enter your age: "))

            match age:
                case _ if age <= 12:
                    print(" You are a kiddo")
                case _ if 13 <=  age <= 20:
                    print("You are a teenager. ")   
                case _  if 21 <= age <= 50:
                    print(" You are fucking adult ") 
                    
                case _ if 51 <= age <= 121:
                    print("You are old. Take care sir .")    
                case _:
                    print("""   Invalid Age!!!
        Age Must be 1 and 121.""") 
                    
        except ValueError:
            print("Age must be number ")
            continue 
        
        break
    
    
          
          
                
matchCase()
stages()
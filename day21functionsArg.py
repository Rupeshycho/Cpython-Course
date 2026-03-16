def gmean(a = 9, b = 8):
    print(f'The gmean of Numbers: {(a*b)/(a+b)}')

#python is an Interpreter (Lines by Line )
gmean(a=100, b=500)

def average(a , b , c=10):
    print(f'Average: {(a+b+c)/2} ')
average(a=13, b=7)



def Student(fname, lname,  age=int):
    print(f'Full name: {fname} {lname}\nAge: {age}')
Student("Rupesh", "Yadav", 21)


#tuple numbers=(29,2,.....) i for iteration (1st: 90, 2nd: 2 , 3rd: ...)
def averageTuples(*numbers):
    print("Class\n",type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
    print(f'Average is: {sum / len(numbers)}')
averageTuples(90,2)


#Dictionary **
def dname(**name):
    print("Hello,",name["fname"], name["mname"], name["lname"])
dname(fname="Rupesh", mname="Anju", lname="Yadav" )

def dname(**name):
    return "Hello,",name["fname"], name["mname"], name["lname"]
result=dname(fname="Rupesh", mname="Anju", lname="Yadav" )
print(result)

def averageTuples(*numbers):
    print("Class\n",type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
    # print(f'Average is: {sum / len(numbers)}')
    return "First return value > Finish !"
    return f'Average is: {sum / len(numbers)}'
    
c=averageTuples(90,2)
print(c)
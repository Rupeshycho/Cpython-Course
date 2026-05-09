#factorial(5)= 5*4*3*2*1
#factorial(4)= 4*3*2*1
#factorial(3)= 3*2*1

#factorial(0) =1

#factorial(7) = 7* factorial(6)

# 8! = 8 * 7!
# n! = n * (n-1)!

def factorial(n):
        
        if n==0:
            return 1
        else: 
            return n * factorial(n-1)
        
print(factorial(5))
print(factorial(1))


def factorial(n):
    if n==0 | n==1:
        return 1 
    else: 
        return n* factorial(n-1)

n=input("Enter the number: ")
result=factorial(int(n))
print("Factorial of ",n, "using Recursion: ", result)




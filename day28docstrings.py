#docstrings are the strings literals that appear right after the definition of a function, method, class, or module. 
#it must comes after the defnition lines 



def square(n):
    'Docstrings:\nTakes the number and print its squares'
    s= n**2
    print(f"Square of {n} is {s}")

square(int(input("Enter the number: ")))

print(square.__doc__)


#PEP-8 = pythonEnhancementProposal
print("\n Ester Egg => Zen of python ")
import this 
print(this)
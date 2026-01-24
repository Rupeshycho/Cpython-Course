name="Rupesh"
friend="Anju"
anotherFriend="Lovish"
apple=''' He said,  
Hi Rupesh
hey I am good 
I want to eat an apple'''
print("Hello, "+name)
print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
# print(name[6]) #throws an error

print("\n===Membership(in not in)===")
family="RupeshAnjuyadav"
for char in family:
    print(char,end=" ")
    
print("---in enumerate---") 
for index, char in enumerate (family):
    print(f'Index: {index} {char}')   
    
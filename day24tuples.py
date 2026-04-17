tup=(1)
print(type(tup))  # int 

#must use comma for tuple 
tup=(1,)
print(type(tup))

tup=(1,2,3)
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])


tupl=(1,2,3,4,5,67)
#tupl[1]=90  #error , tuple is immutable , can't be changed , NO INDEXING
print(type(tupl), tupl)

#slicing 
print(tupl[1:-1:2])

if 342 in tupl: 
    print("Present Sir!")
else: 
    print("Absent Sir!")
    
tupl2=tupl[1:4]
print(tupl2)


#Every 3rd animals   => Slicing in tuples  ; animals[start index: End Index: Jump step ]
animals=("Cat ", "Dog ", "Elephant ", "Goat " , "Human ", " Orangutan ", "chimpanzee ", "Giraffe", "Rhinocerous ")
print(animals[0:len(animals)-1:3])
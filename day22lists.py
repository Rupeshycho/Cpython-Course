#starts with square brackets []
marks=[3,5,6]     #seprated by commas 
print(type(marks))

print(marks[1]) #indexing 
print(marks[0]) #Unique indexes 
print(marks[2]) 


try: 
    print(marks[5])  #list index out of range 
except:
    print("Value error \n Index out of range  ")

strings=[7,8,"Rupesh"]
print(strings)
print("Negative index -1\n",strings[-1])

#duplicates allowed in lists 
duplicate_list=[1,2,1,1,1,1,1,]
print(duplicate_list) 

if "Rupesh" in strings:
    print("Yes, Available")
else:
    print("Not Available")

if "pes" in "Rupesh": #NO spaces 
    print("yes, Available")
else: 
    print("no")

#slicing in list 
slicing_list=[1,2,3,"Rupesh","AI-Engineer","Data Analyst", "Data Visualization","Data Engineer"]
print(slicing_list[1:-1])  #since upto -1 , -1 similar elements is excluded 

print(slicing_list[0:(len(slicing_list)-1):2]) #Step-index: 2
print(slicing_list[:(len(slicing_list)-1):2]) # : => 0(Starts from 0)

lst=[i for i in range(4)]
print(lst)

listing  =[i*i for i in range(4)]
print(lst)

listing_list = [i for i in range(4)]
print(listing_list)








#Indirectly: tuple => list (add, remove, change) => tuple 
#Tuples are immutable, so first convert it to list then do operations and covert it back to tuple 

countries = ("Spain", "England" , "Nepal" , " India ", " China ")
print("Tuple: ", countries)
#li_countries =list("Spain", "England" , "Nepal" , " India ", " China ") #Not allowed
li_countries=list(countries)
print("List: ", li_countries)


li_countries.append("Nigeria")
print("\nNigeria Added. \nList: ", li_countries)


li_countries.pop(3)  #index of india  ❌(" India ") 
print("\nIndia poped out of the List with li_countries.pop(3):","\n",li_countries)

li_countries[1]="Australia"
print("England => Australia: ","\n",li_countries)

print("List => Tuple")
tup_countries= tuple(li_countries)
print("Countries in Tuple:\n",tup_countries)

countries1= ("Pakistan", "Afghanistan", "Bangladesh", "Sri-Lanka")
countries2=("Vietnam", "India" ,"China")
southEastAsia= countries1+countries2
print(southEastAsia)

li_sea=list(southEastAsia)
li_sea.append("India")
print(li_sea)
print("India is repeated: ",li_sea.count("India"),"times.")

tup_sea=tuple(li_sea)
print("Tuple SEA: ", tup_sea)

#index () method returns the occurance of the item 
tup_num=(0,1,2,3,40,5,4,5,6,7)

#tuple.index(element, start, end)
# (start, end )= slice first then find the  occurance between the slicin 
print("Tuple: ", tup_num)
print("Orginally Index of 5: ",tup_num.index(5))
tup_len= len(tup_num)
print("Length of tuple: ", tup_len)

print("Index of last occuring 5: ", tup_num.index(5, 6,9))







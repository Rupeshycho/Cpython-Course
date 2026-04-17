l=[1,2,3,4,5,6]

#App+ end = Add to the end 
l.append(7)

print(l)

lst=[11,45,678,987,98,1,2,3,4,5,6,7,8,9]

#Ascending order
lst.sort()   
print(lst)

#Descending order reverse = True 
lst=[1,2,3,4,5,5,6,7,8,9,12,13414,123412324]

descending=lst.sort(reverse=True) #None
print(descending)

lst.sort(reverse=True)
print("\nIn descending: ",lst)

#List methods is used to add at the end (append), sort (Ascending and Descending)
#reverse()
new_list=[1,2,3,4,5,6,7,8,8,8,9,10]
new_list.reverse()
print(new_list)

#index()   => prefer 1st occurrence
list2=[1,2,3,4,5,6,7,5]

print(list2.count(5))
print("Index of 5: ",list2.index(5))

list3=list2.copy()
list3[0]=0
print("Copy List with 0 at 0th index: ", list3)

#insert(index, num or string)
list3.insert(-1, "last")
print(list3)


#extend()  =>  append whole list items to the end 
ls=[1,2,3,4]
m=[1000,2000,30000,4000]
print(m+list3)
ls.extend(m)
print(ls)   
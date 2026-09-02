
#Do not allows duplicate values 
st={'rupesh':90,'anju':99,'anju':90}
print(st)

print(type(st))

#set are unordered collections of data 
un_set={False, "Rupesh", 0.9, 9 , 9}
print(type((un_set)))
print(un_set)

rupesh={}
print(type(rupesh))

for value in un_set:
    print(value)

s1={1,2,5,6}
s2={3,4,5}
print(s1.union(s2))
print(s1,s2)
s1.update(s2)
print(s1)

cities={"ktm","Bhaktapur", "lalitpur"}
cities2={"ktm","kavre", "lalitpur", "lagankhel"}
print(cities.union(cities2))


towns1={"ktm", "manchester", "berlin", "madrid"}

towns2={"ktm", "madrid"}
print(towns1.intersection(towns2)) #returns a new set
print(towns1.intersection_update(towns2)) #modifies the set


cities1={"madrid", "chelsea", "seoul", "rajbiraj"}
cities2={"madrid", "seoul", "ktm", "lalitpur"}
print(cities1.symmetric_difference(cities2))

print(cities1.difference(cities2))


s= {2,4,2,6}
print(s)

setA = {"Rupes", "Anju", "Arjun"}
setB={"Rupes", "Anju", "Yadav"}
# print(setA.union(setB))
setc=setA.copy()+setB.copy()
print(setc)


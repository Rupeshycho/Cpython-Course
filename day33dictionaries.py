dict1={
    "name": "Rupesh",
    "age":30
}
print(dict1)

dict2={
    1:"Rupesh",
    2:"anju",
    3:"Anju"
}
for i in dict2.keys():
    print(dict2[i])

info =  { 
    "name": "Rupesh",
    "age":19, 
    "eligible_to_vote": True
}
print(info.keys())
print(info.values())

for key in info.keys():
    print(f'The value of key for {key} is {info[key]}')

print(info.items())

for key, value in info.items():
    print(f'The value for {key} is {value}')


info2={"car":"audi","model":"triumph"}
print(info2['car'], "car has the mode ",info2["model"])

# 1.Dictionary are using key value pairs to store values 
# 2. They are made by using s1={"key":"Value","key":"Value"} syntax
# 3. to get all keys of dictionary:  dict1.keys()
# 4. to get all the values of dictionary: dict1.values()
# 5. to get all the pairs : dict1.items()
# 6. dict1['key'] gives the value for the respective key but 
# info.get("key") also return the value but doesnot throw an error if not found 


dict= {
    "name": "Anju", 
    "class": 13,
    'roll': 12
    }
print(dict.items())
print("The Roll No.:", dict['roll'])
print(dict.get('roll'))
print(dict.keys())

for key in dict.keys(): 
    print('The value corresponding to the ',key, 'is', dict[key])


for key, value in dict.items(): 
    print(f'The value corresponding to the {key} is {value}')
    

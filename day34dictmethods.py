ep1 = {'emp1': 'John', 'emp2': 'Jane', 'emp3': 'Doe'}
ep2 = {'emp4': 'Alice', 'emp5': 'Bob'}

del ep2['emp5']
print(ep2)
ep1.update(ep2)
print(ep1)  # Output: {'emp1': 'John', 'emp2': 'Jane', 'emp3': 'Doe', 'emp4': 'Alice', 'emp5': 'Bob'}

ep1.pop("Jane popped out of the dictionary: ", 'emp2')

ep1.popitem()  # Removes the last inserted key-value pair
ep1.clear()

print("The empty dictionary is:", ep1)  # Output: {}

empty_dictionary= {}
print("The empty dictionary is:", empty_dictionary)  # Output: {}   

print("The dictionary of ep2", ep2)  # Output: {'emp4': 'Alice', 'emp5': 'Bob'}
del ep2 
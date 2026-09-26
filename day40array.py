#An array can be created by using the array module (for basic arrays) or numpy ( commonly used )
# you need to specify the data type of the array elements while creating an array using the array module 
# once created,  you can access elements using their index, starting from 0 

from array import array 
arr =array('i', [10,  20, 30 , 40])
print(arr[0]) # prints 10

# i stands for integer, you can use other data types like 'f' for float, 'd' for double, 'u' for unicode char and 'b' used for signed char

#printing all i, f, d, and u type arrays
arr1 = array('i', [1, 2, 3, 4, 5])
arr2 = array('f', [1.1 ,2.2, 3.3, 4.4, 5.5])
print(f' Array f: {arr2[2]}')
arr3 = array('d', [1.11, 2.22, 3.33, 4.44, 5.55])
for a in range(len(arr3)): 
    print(f' Term {a} in Array double: {arr3[a]}')


import numpy as np
num1 = np.array([1, 2, 3, 4, 5])
num2 = np.array([2,3,4,5,6])
sum = num1+num2
print(f' Num1: {num1} \n Num2: {num2} \n Sum: {sum}')

#print the numpy array as it is 
print(f' Numpy array without commas : {num1} \n Numpy array with commas: {num1.tolist()}')

empty_array = np.empty(5)
print(f' Empty array: {empty_array}')

empty_array1 = np.empty((2, 3))
print(f' Empty array with 2 rows and 3 columns: {empty_array1}')


zeros = np.zeros(5)
ones = np.ones(5)
print(f'The zeroes: {zeros}')
print(f'Ones {ones}')


#An array is a collection of elements of the same data type stored in a contiguous ( next to each other) memory locations. 

#Each element can be accessed using an index (position), and indexing usually starts from 0. 

#Arrays are commonly used in many programming languages for efficient storage and access . 

# Arrays should be of same data tupes ,stored in contigous memory locations , it is of fixed size ( in many languages ), Generally faster , less flexible , used for better performance. 
#List can stoore different data types( heterogeneous ), not necessarily contiguous(next to each other) , its dynamic (grow or shrink),  slightly slower in performance, its more flexible because it can adapt to changes in the number of elements , used for general purpose programming


#Each element in an array has an index(position)
# Indexing in python starts from 0,, 
# You can access individual elements using the index inside square brackets []
#You can also use negative indexing to access elements from the end. 

import numpy as np 

array1 = np.array([10,20,30,40,50])
print(array1[0])
print(array1[-1])
print(array1[1:4]) #slicing the array from index 1 to 3 (4 is exclusive)
print(array1[:3]) #slicing the array from index 0 to 2 (3 is exclusive)
print(array1[2:]) #slicing the array from index 2 to the end
print(array1[:]) #slicing the array from index 0 to the end
print(array1[::2]) #slicing the array with a step of 2 (every second element)


arrays = np.array([10, 2, 30, 4 , 50])
for num in arrays: 
    print(num)

for i in range(len(arrays)):
    print(f' Index {i}: {arrays[i]} ')

for i, num in enumerate(arrays):
    print(f' Index {i}: {num}')

narr = np.array([10, 20, 30])
narr2 = np.array([20,40])
new_arr = np.concatenate((narr, narr2))
print(f' Concatenated arrays: {new_arr}')
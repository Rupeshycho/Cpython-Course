# import pandas as pd   

# data = { 'Name': ["Rupesh", "Anju"], "Age" :[21,18]}
# df = pd.DataFrame(data)
# print(df)


# from matplotlib import pyplot as plt 

# x_values= [1,2,3,4,5,3,5,6]
# y_values = [10,12,34,65,31,45,65,90]

# plt.plot(x_values, y_values)   #it shows the connected line, or curves. 

# other_xvalues=[1,2,3,4,5]
# other_yvalues = [3,4,5,6,7]

# plt.scatter(other_xvalues, other_yvalues, color= "red")

# plt.title("Plot & Scatter  ", color='blue')

# plt.xlabel(" X Values ", fontweight='bold')

# plt.ylabel(" Y Values ", fontweight='bold')

# plt.show()



# from matplotlib import pyplot as plt

# values1= [10,20,30,40,50]
# values2=[60,70,80,90,110]

# plt.scatter(values1,values2, color='blue')
# plt.show()

# from matplotlib import pyplot as plt 

# import numpy as np   
# value1=np.array(range(1,6))
# value2=np.array(range(9,14))


n = int(input("Enter the number : "))
n=n%2
if n==0:
    print("Even Number")
else:
    print("Odd number ")


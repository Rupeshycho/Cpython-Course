#creating a python program capable of greeting you with
# good Morning, good afternoon and good evening. Your program should use time module
# to get the current hour. here is a sample program and documentation link for you: 


import time 

# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)


# hour = int(time.strftime("%H"))

# print("its",hour ,"hours")

# if hour<12:
#     print("Good morning")
    
# elif 12<=hour<16:
#     print("Godo Afternoon! ")
    
# elif 16<hour<24:
#     print("Good Night \n ZZZZZZZZZZZZZZZzZZzzz")
    

# hour = int(input("Enter hour (0-23): "))

# if hour < 12:
#     print("Good Morning")

# elif 12 <= hour < 16:
#     print("Good Afternoon!")

# elif 16 <= hour < 24:
#     print("Good Night")
 

t = time.strftime('%H:%M:%S')
hour = int(time.strftime("%H"))
print(hour)

if 0<=hour<12:
    print("Good morning")
elif 12<=hour<16:
    print("Good afternoon")

elif 16<=hour<23:
    print("Good Evening")
else:
    print("Good night")
    


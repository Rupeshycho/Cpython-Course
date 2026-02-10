#strftime = string Format time 

import time
userName=input("Enter your name:\n")

recentime=(time.strftime('%H:%M:%S'))

greetTime=int(time.strftime('%H'))
c = userName.capitalize()

if(4<=greetTime<=12):
    print(f'Good Morning, {userName} its {recentime}')
    
elif (12<=greetTime<=17):
    print(f'Good Evenin, {userName} its {recentime}') 
else: 
    print(f'its {recentime} Goodnight, {userName}')   


# import time
# time= time.strftime('%H:%M:%S')
# print(time)
# if (time>='06:00:00' and time<='11:59:59'):
#     print('Good Morning')
#     if time<='07:00:00':
#         print("You are up early, break-fast will be ready soon")
#     elif time>='07:00:01' and time<'09:00:00':
#         print('Do you want to have break-fast?')
#     elif time<='09:30:00':
#         print('You barely made for break-fast')
#     else:
#         print('You are late! Break-fast time is over')
# elif time >= '12:00:00' and time<='15:59:59':
#     print('Good Afternoon')
#     if time<='02:00:00':
#         print('Do you want to have some tea/coffee?')
#     else:
#         print('It is lunch-time, can I serve you lunch?')
# elif time >='16:00:00' and time<='19:29:59':
#     print('Good Evening')
#     if time<'17:00:00':
#         print('Do you want tea?')
#     elif time>'17:00:00' and time<'19:00:00':
#         print("Let's go to the gym")
#     else:
#         print("Let's have some fun")
# elif time >='19:30:00' and time<='22:00:00':
#     print('Good Night')
#     if time<'20:29:59':
#         print("It's fun time")
#     else:
#         print("It's Dinner time, let's eat!")
# else:
#     print('''Good Night!
#           Sleep Time, 
#           Go to bed''')

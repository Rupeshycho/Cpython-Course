for i in range(1,6):
    print(i)
    
#while loop
print('While Loop Example'.center(40,'-'))
i =1
while i<7:
    print(i)
    i=i+1
print('Done with the loop. ')




i =int(input("Enter a number to count up to: "))
while i<=30:
    i=int(input("Enter a number to count up to:  (30)") )
    print(i)
    i=i+1
print("MUST BE LESS OR EQUAL TO 30. ")



count=5
while count>0:
    print(count)
    count=count-1
else:
    print('else commmand runed ')


number= 0
while number!=7:
    number= int(input("Enter the magic number in the Universe: "))
print("Yes it is , Congrats!!!")


while True: 
    magic_num=int(input('Enter the magic number in the Universe: '))
    if magic_num==7:
        print("         Congratulations🍾👏🎉\n7: continents, colors in a rainbow , Ronaldo suiiiiii")
        break    #Exit the loop 
    else:
        print("Try again!")  #prompt use to keep guessing 

i=0
while True: 
    i = int(input("Enter the Mysterious number?\n "))
    if i!=7:
        print(f'Hint: Suiii!!🫨')
    else:
        print("\nCongratulations👏\nRonaldo , Rainbow, Continents  &  Dhoni ")
        break
    

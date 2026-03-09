for i in range(15):
    if(i==10):
        print(f'{5*i} Easy. 0 after 5')
        continue
    print(f'5x{i}={i}')
    i+=5

i=0
while True:
    print(i)
    i+=1
    if(i==100):
        print("100* | Century")
        break
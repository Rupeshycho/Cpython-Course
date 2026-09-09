
try:
    a = int(input("Enter a number: "))
    print("Multiplication table of {} is:".format(a))
    for i in range(1,11):
        print(f'{a}*{i} = {a*i}')
    print("Multiplication ended for {}.". format(a))
except Exception as e:
    print(f" It should be a number!!!")



try: 
    num = int(input("Enter a number: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer. ")
except IndexError:
    print("Index Error!")
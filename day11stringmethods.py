
print("rupex".capitalize())         #Rupex
print("Hello Rupex".casefold())  #hello rupex
print("hello World". center(20)) #'    hello World     '
print("hello World".count("l"))  #2
print("hello World" .encode())        #b'hello World'
print("hello World" .endswith('.'))     #False
print("H\te\tl\tl\to". expandtabs(4))    #H   e   l   l   o
print("hello World" .find('Wor'))        #6
print("{price:.2f}$".format(price=49))    #49.00$
print("hello World" .index('Wor'))        #6
print("hi World" .replace("World","Tom")) #hi Tom
print("hello World 20" .isdigit())  #False
print("Complex" .isalpha()) #True
print("50" .zfill(10)) #0000000050
print("hello Instagram" .upper()) #HELLO INSTAGRAM
print("I'm Rupesh" .swapcase()) #i'M rUPESH
print(b'hello world'.decode()) #hello world
print("chatgpt4" .isalpha()) #False
print("chatgpt4" .isascii()) #True
print("chatgpt4" .isdecimal())  #False
print("hello_world" .isidentifier())     #True
print("hello_World" .islower())       #False
print("Hi!\nAre you.#1?" .isprintable()) #False 
print('    '.isspace())                  #True 
print("Water" .maketrans("W", "S"))      #{87: 83}
print("Hello Stark" .rjust(10))          #Hello Stark
print("Harry & Ginny" .rpartition("&"))  #('Harry ', '&', ' Ginny')
print("Hare Krishna" .startswith("Hare"))#True
print("'Har' 'Har' 'Mahadev'".rsplit("🙏")) #["'Har' 'Har' 'Mahadev'"]
print("Hello\nFriends".splitlines()) #['Hello', 'Friends']

a =input("Email Address: ")
div=a.partition("@")
print(f'Your name is: {div[0].title()}')
#wap to display questions to the user like KBC
 # use list data type to store the questions and their correct answers. 
# Display the final amount the person is taking home after playing the game 
#Normal 
print("""What is the capital of Nepal ?   
1. Biratnagar
2. Itahari
3. Dharan
4. Kathmandu 
      """)

option=int(input("Enter the correct Option(1-4):\n"))

if option == 4:
    print("Congrats!!! ")
    print("You won Rs. 15000/-")
else:
    print("Wrong, You loose. ")


#list-type
questions =  [
    "Capital of Nepal?\n1. Biratnagar\n2. Itahari\n3. Dharan\n4. Kathmandu",
    "Capital of India?\n1. Mumbai\n2. Delhi\n3. Kolkata\n4. Chennai",
    "Capital of Japan?\n1. Seoul\n2. Tokyo\n3. Beijing\n4. Bangkok"
]
answers = [4,2,2]
money = [10000, 15000, 25000]
score = 0 

for i in range(len(questions)):
    print(questions[i])
    
    option= int(input("Enter the correct option(1-4): "))
    
    if option == answers[i]:
        print("Correct! ")
        score+=money[i]
    
    else:
        print("Wrong Answer! ")
        break
print("\n     Final Amount You Take home: RS. ", score, "/-")
    



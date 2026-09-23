questions = [
    ["Which language is used to create Facebook?",
     "Python", "French", "JavaScript", "C++", 4],

    ["Which language is used to create Instagram?",
     "Python", "French", "C++", "JavaScript", 1],

    ["Which language is used to create WhatsApp?",
     "Python", "French", "JavaScript", "C++", 4],
]

levels = [10000, 15000, 25000]

money = 0

for i in range(len(questions)):

    question = questions[i]

    print("\n-----------------------------")
    print(f"Question for Rs. {levels[i]}/-")
    print(question[0])

    # question[1] to question[4] are the options
    # question[5] is the index containing the correct answer

    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    option = int(input("Enter the correct option (1-4): "))

    if option == question[5]:
        print("Correct Answer! 🎉")
        money = levels[i]
        print(f"You won Rs. {money}/-")

    else:
        print("Wrong Answer! ❌")
        print(f"Game Over! You won Rs. {money}/-")
        break

else:
    print("\n🎉 Congratulations! 🎉")
    print(f"You won Rs. {money}/-")
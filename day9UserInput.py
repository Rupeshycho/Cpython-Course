# a= input("Enter your name: ")
# print("Hello, ",a,"!\Welcome sir 🙏")

# x=input("Enter first number: ")
# y=input("Enter second number: ")
# print(f'x+y= {x+y} (no addition cause its in string , USE: int(input("...")))')


# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# print("Quotient: ",a//b,"\n(without any remainder)")

# USER INPUT PRACTICE 

print("Welcome to User Input Practice Program")
print("-" * 40)

name = input("Enter your name: ")
print("Hello,", name)

# 2. Taking integer input
age = int(input("Enter your age: "))
print("You are", age, "years old")

# 3. Taking float input
height = float(input("Enter your height in cm: "))
print("Your height is", height, "cm")

# 4. Simple condition
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

print("-" * 40)

# 5. Multiple inputs
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Floor Division:", a // b)
print("Remainder:", a % b)

print("-" * 40)

# 6. Loop with user input
n = int(input("Enter how many times to print your name: "))
for i in range(n):
    print(i + 1, name)

print("-" * 40)

# 7. Password validation
password = input("Create a password: ")

if len(password) < 6:
    print("Password too short")
else:
    print("Password accepted")

print("-" * 40)

# 8. Taking list input
numbers = []
count = int(input("How many numbers do you want to enter? "))

for i in range(count):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Numbers entered:", numbers)
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Average:", sum(numbers) / len(numbers))

print("-" * 40)

# 9. Menu-driven program
while True:
    print("\nMENU")
    print("1. Check even/odd")
    print("2. Square a number")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        x = int(input("Enter a number: "))
        if x % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

    elif choice == "2":
        x = int(input("Enter a number: "))
        print("Square:", x * x)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")

print("-" * 40)

# 10. Final message
print("User input practice completed!")

def greet():
    return "Hello!"

say_hello = greet   # assigning function to a variable

print(say_hello())  # calling the function using the new name

def mult(n):
    return lambda a: a*n

doupler =mult(5)
tripler= mult(6)
print(doupler(2))
print(tripler(6))



price=int(input("Enter the price of your T-shirt: "))
discount = lambda price: price* 0.9
print(discount(price))



#FullcodeToUnderstandLambdaFunction

prices = list(map(int, input("Enter T-shirt prices (space-separated): ").split()))

apply_discount = lambda price: price * 0.9
add_tax = lambda price: price * 1.13

discounted_prices = list(map(apply_discount, prices))
final_prices = list(map(add_tax, discounted_prices))

expensive_items = list(filter(lambda price: price > 1000, final_prices))

sorted_prices = sorted(final_prices, key=lambda x: x)

print("\nOriginal Prices:", prices)
print("After Discount:", discounted_prices)
print("After Tax:", final_prices)
print("Expensive Items:", expensive_items)
print("Sorted Prices:", sorted_prices)

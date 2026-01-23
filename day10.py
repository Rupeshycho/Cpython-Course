# IMPLICIT TYPECASTING (Automatic)

a = 10          # int
b = 5.5         # float

c = a + b       # int + float → float (implicit)
print("Implicit Typecasting:")
print("a (int) + b (float) =", c)
print("Type of c:", type(c))

print()

# EXPLICIT TYPECASTING (Manual)

x = 12.75
y = int(x)      # float  int

num = "100"
z = int(num)    # str  int

f = float(z)    # int float

print("Explicit Typecasting:")
print("float to int:", y)
print("string to int:", z)
print("int to float:", f)
print("Typecasting demo\n")

a = 10
b = 4.5
c = a + b
print(c, type(c))

x = True
y = 7
z = x + y
print(z, type(z))

m = 5
n = 2 + 3j
o = m + n
print(o, type(o))

p = 15.99
q = int(p)
r = float(q)
s = str(p)
print(q, type(q))
print(r, type(r))
print(s, type(s))

num = "120"
i = int(num)
f = float(num)
print(i, type(i))
print(f, type(f))

text = "python"
chars = list(text)
print(chars, type(chars))

nums = [1, 2, 3, 3, 4]
tup = tuple(nums)
st = set(nums)
string_form = str(nums)
print(tup, type(tup))
print(st, type(st))
print(string_form, type(string_form))

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("AI"))
print(bool([]))
print(bool([10]))

price = "99.50"
qty = "4"
total = float(price) * int(qty)
print(total, type(total))

value = "45x"
try:
    result = int(value)
    print(result)
except ValueError:
    print("conversion failed")

age = int(input("Enter age: "))
height = float(input("Enter height: "))
print(age, type(age))
print(height, type(height))


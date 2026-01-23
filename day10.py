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

#Demo Type casting 
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

def type_casting3():
    
        
    print("===== PYTHON TYPECASTING FULL DEMO =====\n")


    # 1️ IMPLICIT TYPECASTING (Automatic)


    print("1. IMPLICIT TYPECASTING")

    a = 10          # int
    b = 3.5         # float
    c = a + b       # int → float automatically

    print("a =", a, type(a))
    print("b =", b, type(b))
    print("a + b =", c, type(c))

    # Boolean + Integer
    x = True
    y = 5
    z = x + y       # True → 1
    print("\nTrue + 5 =", z, type(z))

    # Integer + Complex
    m = 4
    n = 2 + 3j
    o = m + n       # int → complex
    print("int + complex =", o, type(o))

    print("\n" + "-"*40 + "\n")


    # 2️ EXPLICIT TYPECASTING (Manual)


    print("2. EXPLICIT TYPECASTING")

    p = 12.99
    q = int(p)      # float → int (loss of data)
    r = str(p)      # float → string

    print("float to int:", q, type(q))
    print("float to str:", r, type(r))

    # String to numeric
    s = "250"
    t = int(s)
    u = float(s)

    print("\nstring to int:", t, type(t))
    print("string to float:", u, type(u))

    print("\n" + "-"*40 + "\n")


    # 3️TYPECASTING WITH COLLECTIONS


    print("3. TYPECASTING WITH COLLECTIONS")

    nums = [1, 2, 3, 4]
    nums_tuple = tuple(nums)
    nums_set = set(nums)
    nums_str = str(nums)

    print("list → tuple:", nums_tuple)
    print("list → set:", nums_set)
    print("list → string:", nums_str)

    # String to list (twist)
    text = "python"
    char_list = list(text)
    print("\nstring → list:", char_list)

    print("\n" + "-"*40 + "\n")


    # 4️. USER INPUT TYPECASTING

    print("4. USER INPUT TYPECASTING")

    age = int(input("Enter your age: "))
    height = float(input("Enter your height in meters: "))

    print("Age:", age, type(age))
    print("Height:", height, type(height))

    print("\n" + "-"*40 + "\n")

    #  ERROR & EXCEPTION HANDLING (BIG TWIST)


    print("5. TYPECASTING ERRORS & HANDLING")

    value = "10a"

    try:
        number = int(value)
    except ValueError:
        print("Error: Cannot convert '10a' to integer")

    print("\n" + "-"*40 + "\n")

    #boolean typecasting 
    print("6. BOOLEAN TYPECASTING")

    print("bool(0) =", bool(0))
    print("bool(1) =", bool(1))
    print("bool('') =", bool(""))
    print("bool('Python') =", bool("Python"))
    print("bool([]) =", bool([]))
    print("bool([1,2]) =", bool([1,2]))

    print("\n" + "-"*40 + "\n")

    #real word mini scenario
    print("7. REAL-WORLD EXAMPLE")

    price = "99.99"
    quantity = "3"

    total = float(price) * int(quantity)

    print("Price:", price)
    print("Quantity:", quantity)
    print("Total cost:", total)

    print("\n===== END OF DEMO =====")

type_casting3()

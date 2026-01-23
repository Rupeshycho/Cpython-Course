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

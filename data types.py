# Numbers
a = 10 # int
b = 10.0 # float
c = 10 + 5j # complex a+ib--->a+bj
d = True # bool
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# String / str
name = "Sriti"
print(type(name))

# List
numbers = [10,20,30]
print(type(numbers))

# Tuple
numbers = (10,20,30)
print(type(numbers))

# Set
numbers = {10,20,30}
print(type(numbers))

# Dictionary / dict
numbers = {1:"one", 2:"two"}
print(type(numbers))

# NoneType
value = None
print(type(value))

# Typecasting
# Implicit Casting
x = 10
y = 10.5
z = x + y
print(type(x))
print(type(y))
print(type(z))
# Explicit Casting
x = 10
y = 10.5
z = x + int(y)
print(type(x))
print(type(y))
print(type(z))

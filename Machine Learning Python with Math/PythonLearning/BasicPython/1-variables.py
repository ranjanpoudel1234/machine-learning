myInt = 7
print(myInt)

myFloat = 7.0
print(myFloat)

# Add numbers
print(myInt + myFloat) # 14.0


myString = "Hello"
print(myString)

myStringWithQuotes = 'He said, "Hello!"'
print(myStringWithQuotes)

# Concatenate strings
print(myString + " World!") # Hello World!

myBool = True
print(myBool)

myList = [1, 2, 3, 4, 5]
print(myList) # [1, 2, 3, 4, 5]

# multiple variable assignment in one line
a, b, c = 10, 20.5, "Python"
print(a)      # 10
print(b)      # 20.5
print(c)      # Python

# This will not work! Cannot mix operand types
one = 1
two = 2
hello = "hello"

# print(one + two + hello) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Exercise
mystring = "hello"
myFloat = 10.0
myInt = 20

# testing code
if mystring == "hello":
    print("String: %s test %s " % (mystring, mystring))
if isinstance(myFloat, float) and myFloat == 10.0:
    print("Float: %f" % myFloat)
if isinstance(myInt, int) and myInt == 20:
    print("Integer: %d" % myInt)
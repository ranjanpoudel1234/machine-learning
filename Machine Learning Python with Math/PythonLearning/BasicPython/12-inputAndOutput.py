## Receiving input and producing output in Python

# string = input("Enter something: ")  # input() reads a line from input, converts it to a string (stripping a trailing newline), and returns that.
# print("You entered:", string)  # print() outputs to the console or other standard output

# a, b = input("Enter two numbers separated by space: ").split()  # split() splits the input string into a list where each word is a list item
# print("You entered:", a, b)

# a, b = map(int, input("Enter two numbers separated by space: ").split())  # map() applies the int function to each item in the list
# print("Sum:", a + b)

# a = 5
# b = 0.63
# c = "hello"
# print("a is : %d b is %0.4f c is %s" % (a,b,c))

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello, %s! You are %d years old." % (name, age))
print ("Hello, my name is {}, I am {} years old.".format(name, age))
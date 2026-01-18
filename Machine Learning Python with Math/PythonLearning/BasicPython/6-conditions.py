## and and or operators
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

## the in operator
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

## if else 
statement = False
another_statement = True
if statement == True:
    # do something
    pass
elif another_statement is True: # else if, can also use ==
    print("Another statement is true")
    # do something else
    pass
else:
    # do another thing
    pass
## make each if return true

number = 16
second_number = False
first_array = [1, 2, 3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
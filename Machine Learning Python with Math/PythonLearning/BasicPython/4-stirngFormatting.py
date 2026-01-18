# This prints out "John is 23 years old."
# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)
name = "John"
age = 23
weight = 150.5
print("%s is %d years old." % (name, age))
print(f"{name} is {age} years old.") # modern version of formatting
print("%s is %d years old. He weighs %f lbs." % (name, age, weight)) # John is 23 years old. He weighs 150.500000 lbs.
print("%s is %d years old. He weighs %.1f lbs." % (name, age, weight)) # John is 23 years old. He weighs 150.5 lbs.

print(f"{name} is {age} years old. he weights {weight}lbs") # modern version of formatting

#Exercise, Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."


print(format_string % data) # wow, you can provide entire tuple here
## The Map Function

my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []

for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)

print(uppered_pets)

## With map function
# Python 3
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)

# Python 3


# The range(1, 7) function acts as the second argument to the round function (the number of required decimal places per iteration). 
# So as map iterates through circle_areas, during the first iteration, the first element of circle_areas, 3.56773 is passed along with the first element of range(1,7), 1 to round, making it effectively become round(3.56773, 1). During the second iteration, the second element of circle_areas, 5.57668 along with the second element of range(1,7),
# 2 is passed to round making it translate to round(5.57668, 2). This happens until the end of the circle_areas list is reached.
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1, 7)))

print(result)

result = list(map(round, circle_areas, range(1, 3))) # no error for different lengths

print(result)

### THe zip function
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(zip(my_strings, my_numbers))

print(results)


# Python 3- zip function using map

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)


### Filter

# Python 3
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))

print(over_75)

# Python 3
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)

## Reduce

from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)

#### Map
from functools import reduce 

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_numbers = [4, 6, 9, 23, 5]


# Use map to print the square of each numbers rounded
# to three decimal places
map_result = list(map(lambda x: round(x ** 2, 3), my_floats))

# Use filter to print only the names that are less than 
# or equal to seven letters
filter_result = list(filter(lambda name: len(name) <= 7, my_names))

# Use reduce to print the product of these numbers
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)
## Arithmetic Operators

number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

square = 7 ** 2
print(square) # 49

cube = 2 ** 3
print(cube) # 8

## woah, multiplying strings

lotsOfHellos = "hello" * 10
print(lotsOfHellos) # hellohellohellohellohellohellohellohellohellohello

## Woah, adding lists directly combines them
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers) # [1, 3, 5, 7, 2, 4, 6, 8]

## Form a new list with repeating sequence, similar to string multiplication
print([1,2,3] * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Exercise
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10

big_list = x_list + y_list

print("x_list contains %s objects" %len(x_list))
print("y_list contains %s objects" %len(y_list))
print("big_list contains %s objects" %len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

## modern version of list operators
x_list = [x for _ in range(10)]
y_list = [y for _ in range(10)]
big_list = [item for pair in zip(x_list, y_list) for item in pair]
print("big_list contains %s objects" %len(big_list))
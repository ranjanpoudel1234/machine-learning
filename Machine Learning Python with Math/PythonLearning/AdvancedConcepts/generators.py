# import random

# def lottery():
#     # returns 6 numbers between 1 and 40
#     for i in range(6):
#         yield random.randint(20, 40)

#     # returns a 7th number between 1 and 15
#     yield random.randint(1, 15)

# for random_number in lottery():
#        print("I am here")
#        print("And the next number is... %d!" %(random_number))

## Exercise
# Write a generator function which returns the Fibonacci series. They are calculated using the following formula: The first two numbers of the series is always equal 
# to 1, and each consecutive number returned is the sum of the last two numbers. 
# Hint: Can you use only two variables in the generator function? Remember that assignments can be done simultaneously. The code


a = 1
b = 2
a, b = b, a
#print(a, b)



def get_fib(n):
    a = 0
    b = 1
    counter = 0
    for number in range(n): #[1, 1, 2,3, 5, 8]
        #a, b = b, a + b
        temp = b
        b = a + b
        a = temp
        yield (a)

print("{}".format(list(get_fib(5))))
## Normal Functions

def sum(a,b):
    return a + b

a = 1
b = 2
c = sum(a,b)
print(c)


## Lambda Functions
sum = lambda a, b: a + b


l = [2,4,7,3,14,19]
for i in l:
     isEven = (lambda i: i %2 ==0)
     print (isEven(i))
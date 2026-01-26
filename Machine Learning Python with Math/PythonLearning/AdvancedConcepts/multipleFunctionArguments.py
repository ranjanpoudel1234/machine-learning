## function with arguments

### functions with arguments, one of them receiving a lot of value

def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))

foo(1, 2, 3, 4, 5)


def bar(first, second, third, **options):
    print("Options: %s" % options)
    print("FirstOption: %s" % options.get("red"))

bar(1, 2, 3, red=True, size=10)

## Exercise

def foo(a, b, c, *others):
    return len(others)

def bar(a, b, c, **options):
    if(options.get("magicnumber") == 7):
        return True
    return False

# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")
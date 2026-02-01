### Function that remembers the values in enclosing scopes even if they are not present in memory

# Firstly, a Nested Function is a function defined inside another function. 
# It's very important to note that the nested functions can access the variables of the enclosing scope. However, at least in python, 
# they are only readonly. However, one can use the "nonlocal" keyword explicitly with these variables in order to modify them.

def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():

        "The nested function"
        print(message)

    data_transmitter()

print(transmit_to_space("Test message")) # prints "Test message". This works well as the 'data_transmitter' function can access the 'message'. To demonstrate the use of the "nonlocal" keyword, consider this


def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number # if we do not use nonlocal, the output would be 3 and 9
        number=3
        print(number) # prints 3
    printer()
    print(number) # Prints 3

print_msg(9)

## returning function objects
def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
fun2()
astring = "Hello world!"
print("single quotes are ' '")

print(len(astring)) # 12

## index
astring = "Hello world!"
print(astring.index("o")) # 4

astring = "Hello world!"
print(astring.count("l")) # 3

astring = "Hello world!"
print(astring[3:7]) # lo w
print(astring[:7]) # Hello w
print(astring[3:]) # Hello w
print(astring[3:7:2]) # l


astring = "Hello world!"
print(astring[3:7]) # lo w
print(astring[3:7:1]), # lo w, start stop, step

# reverse a string
astring = "Hello world!"
print(astring[-3:]) # ld!, negative index starts from end
print(astring[-5:-2]) # orl
print(astring[::-1]) # !dlrow olleH

astring = "Hello world!"
print(astring.upper()) # HELLO WORLD!
print(astring.lower()) # hello world!

astring = "Hello world!"
print(astring.startswith("Hello")) # true
print(astring.endswith("asdfasdfasdf")) # false

astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords) # ['Hello', 'world!']
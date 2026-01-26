## Dictionaries


phoneBook = {}
phoneBook["John"] = 938477566
phoneBook["Jack"] = 938377264

print(phoneBook)
print(phoneBook["John"])
print(phoneBook.get("Jack"))
print(phoneBook.get("Jill", "Not found")) # default value if key not found
print("John" in phoneBook) # True
print(phoneBook.keys()) # dict_keys(['John', 'Jack'])

anotherPhoneBook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
print(anotherPhoneBook)

for name, number in anotherPhoneBook.items():
    print(f"hello {name}:{number}")

## Remove specific item
del anotherPhoneBook["Jill"] ## or anotherPhoneBook.pop("Jill")
print(anotherPhoneBook)

## Exercise

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here
phonebook["Jake"] = 938273443
phonebook.pop("Jill")

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")
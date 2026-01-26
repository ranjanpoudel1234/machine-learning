## JSON Serialization

import json
json_string = json.dumps({'name': 'John', 'age': 30, 'city': 'New York'})
print(json_string)

data = json.loads(json_string)
print(data)
print(data['name'])

## There is python proprietary data serialization method called pickle

import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))

## Exercise

import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    # Add your code here
    salaries_json = json.loads(salaries_json)
    salaries_json[name] = salary
    

    return json.dumps(salaries_json)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])


## Exercise

class Vehicle:
    name = ""
    kind = ""
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
    
car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000


car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000

print(car1.description())
print(car2.description())

### The Init

class NumberHolder:
    def __init__(self, number):
        self.number = number

    def show_number(self):
        print("The number is: %d" % self.number)

num_holder = NumberHolder(7)
num_holder.show_number()

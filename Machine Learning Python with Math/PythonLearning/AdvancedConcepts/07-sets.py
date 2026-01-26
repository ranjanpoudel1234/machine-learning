## Sets In Python

### Sets remove duplicates and are unordered collections of unique elements.

a = set(["Jake", "John", "Eric"])
print(a)
b = set(["John", "Jill"])
print(b)

print(a.intersection(b)) # Elements in both a and b
print(a.union(b))        # Elements in either a or b
print(a.difference(b))   # Elements in a but not in b
print(a.symmetric_difference(b)) # Elements in a or b but not both
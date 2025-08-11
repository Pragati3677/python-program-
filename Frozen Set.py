fruits = frozenset(['Apple', 'Banana', 'Dragon fruits'])
vegitable = frozenset(['flower', 'chilly', 'brinjal', 'capsicum'])
# print("Original set:", fruits)
# print("original set of vegitable:", vegitable)
# frozenset.union(fruits and vegitable)
print("List after union:", frozenset.union(fruits, vegitable))

# frozenset.intersection(fruits, vegitable)
print("List after intersection:", frozenset.intersection(fruits and vegitable))

frozenset.copy(fruits)
print("List after copy:", frozenset.copy(fruits))
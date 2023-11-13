# No duplicate value is allowed in sets

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
set3 = set()  # empty set
print(set1)
print(set2)
print(set1.pop())
set1.add(7)
print(set1)
set3 = set1.copy()
print(set3)
print(set2.union(set1))
print(set3.intersection(set2))
print(set2)
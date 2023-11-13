# Tuple is immutable
t1 = (1, 2, 3, 4, 5, 6)
print(t1.count(4))
print(t1.index(3))
print(t1.__getitem__(4))
print(t1[1])
print(t1[1:4])
print(t1[::-1])
s1 = set([1,2,3])
print(s1)

s2 = set("Hello")
print(s2)

l1 = list(s1)
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)
print(t1[0])

s3 = set([1, 2, 3, 4, 5, 6])
s4 = set([4, 5, 6, 7, 8, 9])

s5 = s3 & s4
print(s5)
print(s3.intersection(s4))
print(s3 | s4)
print(s3.union(s4))
print(s3 - s4)
print(s4 - s3)
print(s3.difference(s4))
print(s4.difference(s3))

s1.add(4)
print(s1)

s6 = set([1, 2, 3])
s6.update([4, 5, 6])
print(s6)

s6.remove(2)
print(s6)
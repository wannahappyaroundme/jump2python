odd = [1, 3, 5, 7, 9]

a = []
b = [1, 2, 3]
c = ["Life", "is", "too", "short"]
d = [1, 2, "Life", "is"]
e = [1, 2, ["Life", "is"]]
print(b)

print(b[0])
print(b[0]+b[2])
print(b[-1])

b = [1, 2, 3, ['a', 'b', 'c']]

print(b[0])
print(b[-1])
print(b[3])
print(b[-1][0])
print(b[-1][1])
print(b[-1][2])

b = [1, 2, ['a', 'b', ['Life', 'is']]]

print(b[2][2][0])

b = [1, 2, 3, 4, 5]

print(b[0:2])

b = "12345"

print(b[0:2])

a = [1, 2, 3, 4, 5]

print(a[1:3])

aa = [1, 2, 3]
bb = [4, 5, 6]

print(aa + bb)
print(aa*3)
print(len(aa))
print(str(aa[2])+"hi")

aa[2] = 4

print(aa)

aa = [1, 2, 3]

del aa[1]

print(aa)

aaa = [1, 2, 3, 4, 5]

del aaa[2:]

print(aaa)
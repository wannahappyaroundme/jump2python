a = 1
b = "python"
c = [1, 2, 3]

print(id(c))

d = c
print(id(c))
print(id(d))

print(c is d)

c[1] = 4

print(c)
print(d)
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

e = [1, 2, 3]
f = e[:]
e[1] = 4
print(e)
print(f)

from copy import copy

g = [1, 2, 3, 4]
h = copy(g)
print(g)
print(h)

print(g is h)
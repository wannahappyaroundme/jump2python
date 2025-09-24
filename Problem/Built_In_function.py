print(abs(3))
print(abs(-3))
print(abs(-1.2))
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))
print(all([]))
print(any([1, 2, 3, 0]))
print(any([0, ""]))
print(any([]))
print(chr(97))
print(chr(44032))
print(dir([1, 2, 3]))
print(dir({'1':'a'}))
print(divmod(7,3))
print(7//3)
print(7%3)
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
print(eval('1 + 2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))
print(hex(234))
print(hex(3))

aa = 3
print(id(3))
print(id(aa))
bb = aa
print(id(bb))

aaa = input()
print(aaa)

bbb = input("Enter: ")
print(bbb)

print(int('3'))
print(int(3.4))
print(int('11', 2))
print(int('1A', 16))

class Person: pass

abc = Person()
print(isinstance(abc, Person))

dge = 3
print(isinstance(dge, Person))
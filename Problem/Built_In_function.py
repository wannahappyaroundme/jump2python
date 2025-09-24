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

print(len("python"))
print(len([1, 2, 3]))
print(len((1, 'a')))

print(list("python"))
print(list((1, 2, 3)))

ccc = [1, 2, 3, 4]
ddd = list(ccc)
print(ddd)

print(max([1, 2, 3]))
print(max("python"))

print(min([1, 2, 3]))
print(min("python"))

print(oct(34))
print(oct(12345))

# 바이너리 모드로 읽기 b = 바이너리 / r = 읽기 / w = 쓰기 / a = 추가모드
# f= open("binary_file", "rb")

print(ord('a'))
print(ord('가'))

print(pow(2, 4))
print(pow(3, 3))

print(list(range(5)))
print(list(range(5, 10)))
print(list(range(1, 10, 2)))
print(list(range(0, -10, -1)))

print(round(4.6))
print(round(4.2))
print(round(5.678, 2))

print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))
print(sorted("zero"))
print(sorted((3, 2, 1)))

print(str(3))
print(str('hi'))

print(sum([1, 2, 3]))
print(sum((4, 5, 6)))

print(tuple("abc"))
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))

print(type("abc"))
print(type([]))
print(type(open("test", 'w')))

print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def")))
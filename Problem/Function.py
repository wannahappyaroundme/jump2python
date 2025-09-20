def add(a, b):
    return a + b

a = 3
b = 4
c = add(a, b)

print(c)

def say():
    return "Hi"
    
d = say()
print(d)

def add2(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

print(add2(3,4))

add2(3,4)

def say2():
    print("Hi")
    
say2()

def sub(a, b):
    return a - b

result = sub(a=7, b=3)
print(result)
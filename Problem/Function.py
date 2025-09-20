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

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1, 2, 3)
print(result)

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result2 = add_mul('add', 1, 2, 3, 4, 5)
print(result2)

result3 = add_mul('mul', 1, 2, 3, 4, 5)
print(result3)

def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(a=1)
print_kwargs(name='foo', age=3)

def add_and_mul(a, b):
    return a+b, a*b

result4 = add_and_mul(3, 4)
print(result4)

result5, result6 = add_and_mul(3, 4)
print(result5)
print(result6)
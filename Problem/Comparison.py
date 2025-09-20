x = 3
y = 2
print(x>y)
print(x==y)
print(x!=y)

money = 2000

if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
    
money2 = 2000
card = True

if money>=3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
    
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

print('a' in ('a', 'b', 'c'))

print('j' not in 'Python')

pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
    
if 'card' not in pocket:
    print("걸어가라")
else:
    print("버스를 타고 가라")
    
# 아무것도 실행을 안 하고 싶을 떄는 "pass" 를 사용하자
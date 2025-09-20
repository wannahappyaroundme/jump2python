a = True
b = False
print(type(a))
print(type(b))
print(1==1)
print(2>1)
print(2<1)

# 빈 칸이거나 None, Null일 경우에는 False 출력 그 외 나머지는 다 True 출력

c = [1, 2, 3, 4]
while c:
    print(c.pop())
    
if [1, 2, 3]:
    print("참")
else:
    print("거짓")
# 양의 정수 대입
a = 123

# 음의 정수 대입
b = -178

# 0 대입
c = 0

# 4.24e10과 4.24E10은 동일
# 4.24 x 10^10
d = 4.24e10
e = 4.24E10
# True
print(d==e)


# 4.24e-10과 4.24E-10은 동일
# 4.24 x 10^-10
f = 4.24e-10
g = 4.24E-10
# True
print(f==g)

# 8진수
h = 0o177
# 127
print(h)

# 16진수
i = 0x8ff
j = 0xABC
# 2303
print(i)
# 2748
print(j)

# 사칙연산

k = 3
l = 4
# 7
print(k+l)

# -1
print(k-l)

# 12
print(k*l)

# 0.75
print(k/l)

# 제곱

# 81
print(k**l)

# 예제
# 3262
print(10*18**2+2*11)

print(7%3)  # 1
print(3%7)  # 3
print(7/4)  # 1.75
print(7//4) # 1

# 예제
# 몫 4, 나머지 2
print(14//3)
print(14%3)
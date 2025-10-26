# 1
# a:b:c:d -> a#b#c#d

text = "a:b:c:d"
A = text.split(":")
answer = "#".join(A)

print(answer)

# 2
# key에 해당하는 value를 출력하는 프로그램

a = {'A':90, 'B':80}
print(a.get('C', 70))

# 3
# Extend와 + [4, 5]의 차이

a = [1, 2, 3]
a = a + [4, 5]
a.append([4, 5])

# extend() = 원본 수정, +는 새 리스트 생성

# 4

# 5

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result = 0

for i in A:
    if i >= 50:
        result += i
    
print(result)
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
# A학급 학생의 점수를 나타내는 리시트 다음 리스트에서 50점 이상 점수의 총합 

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result = 0

for i in A:
    if i >= 50:
        result += i
    
print(result)

# 5
# 피보나치 수열 만들기

def fibo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    result = [0, 1]
    for i in range(n-2):
        next_num = result[-1]+result[-2]
        result.append(next_num)
    return result
    
n = int(input("몇 항까지 출력할까요?"))
print(fibo(n))

# 6 
# 숫자 총합 구하기

number = input("입력시킬 숫자를 적어주세요 :")
num2 = number.split(",")
sum = 0
for i in num2:
    sum += int(i)
    
print(sum)

# 7
# 한 줄 구구단

gugudan = int(input("구구단을 출력할 숫자를 입력하세요(2~9):"))
for i in range(1,10):
    dan = i * gugudan
    print(dan, end=" ")

# 8

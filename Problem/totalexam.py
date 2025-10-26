# # 1
# # a:b:c:d -> a#b#c#d

# text = "a:b:c:d"
# A = text.split(":")
# answer = "#".join(A)

# print(answer)

# # 2
# # key에 해당하는 value를 출력하는 프로그램

# a = {'A':90, 'B':80}
# print(a.get('C', 70))

# # 3
# # Extend와 + [4, 5]의 차이

# a = [1, 2, 3]
# a = a + [4, 5]
# a.append([4, 5])

# # extend() = 원본 수정, +는 새 리스트 생성

# # 4
# # A학급 학생의 점수를 나타내는 리시트 다음 리스트에서 50점 이상 점수의 총합 

# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# result = 0

# for i in A:
#     if i >= 50:
#         result += i
    
# print(result)

# # 5
# # 피보나치 수열 만들기

# def fibo(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     result = [0, 1]
#     for i in range(n-2):
#         next_num = result[-1]+result[-2]
#         result.append(next_num)
#     return result
    
# n = int(input("몇 항까지 출력할까요?"))
# print(fibo(n))

# # 6 
# # 숫자 총합 구하기

# number = input("입력시킬 숫자를 적어주세요 :")
# num2 = number.split(",")
# sum = 0
# for i in num2:
#     sum += int(i)
    
# print(sum)

# # 7
# # 한 줄 구구단

# gugudan = int(input("구구단을 출력할 숫자를 입력하세요(2~9):"))
# for i in range(1,10):
#     dan = i * gugudan
#     print(dan, end=" ")
# print()

# # 8
# # 파일 읽어서 역순으로 정하기
# f = open('/Users/kyungsbook/Desktop/jump2python/Problem/abc.txt', 'r')
# lines = f.readlines()
# f.close()

# lines.reverse()

# f = open('/Users/kyungsbook/Desktop/jump2python/Problem/abc.txt', 'w')
# for line in lines:
#     line = line.strip()
#     f.write(line)
#     f.write("\n")
# f.close()

# # 9
# f = open('/Users/kyungsbook/Desktop/jump2python/Problem/sample.txt', 'r')
# lines = f.readlines()
# f.close()

# total = 0
# for line in lines:
#     total += int(line)
# average = total /len(lines)

# f = open('/Users/kyungsbook/Desktop/jump2python/Problem/result.txt', "w")
# f.write(str(average))
# f.close()

# # 10
# # 계산기 만들기
# class Calculator:
#     def __init__(self, data):
#         self.data = data
    
#     def sum(self):
#         result = 0
#         for d in self.data:
#             result += d
#         return result
    
#     def avg(self):
#         average = self.sum() / len(self.data)
#         return average

# cal1 = Calculator([1, 2, 3, 4, 5])
# print(cal1.sum())
# print(cal1.avg())

# cal2 = Calculator([6, 7, 8, 9, 10])
# print(cal2.sum())
# print(cal2.avg())        

# # 11
# # 모듈 사용하는 방법
# import sys
# sys.path.append("/Users/kyungsbook/Desktop/jump2python/Problem")
# import mymod

# # 12
# # 오류와 예외 처리, 다음 코드의 실행 겨로가를 예측하고 그 이유를 설명하시오

# result = 0

# try:
#     [1, 2, 3][3]
#     "a" + 1
#     4 / 0
# except TypeError:
#     result += 1
# except ZeroDivisionError:
#     result += 2
# except IndexError:
#     result += 3
# finally:
#     result += 4
    
# print(result)

# 13
# Dashinsert 함수

data = "4546793"
numbers = list(map(lin, data))
result = []
for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers)-1: # 다음 수가 있다면
        is_odd = num % 2 == 1 # 현재 수가 홀수
        is_next_odd = numbers[i+1] % 2 == 1 # 다음 수가 홀수
        if is_odd and is_next_odd: # 연속 홀수
            result.append("-")
        elif not is_odd and not is_next_odd: # 연속 짝수
            result.append("*")
        
print("".join(result))

# 14
# 문자가 연속적으로 반복되는 경우, 그 반복 횟수를 표ㅕ시해서 문자열을 압축하여 표시하기
# 입력 예시 : aaabbcccccca, 출력 예시 : a3b2c6a1

def compress_string(s):
    _c = "" # s 문자열 중 현재 진행 중인 문자를 임시 저장하기 위한 변수
    cnt = 0 # 해당 문자가 몇 번 반복했는지 알 수 있는 카운트 변수
    result = "" # 이 함수의 최종 리턴 문자열(예 : a3b2c6a1)
    for c in s: # 입력받은 문자열 s에서 문자 하나씩 c에 대입
        if c != _c: # 현재 진행 중인 문자와 c가 같지 않은 경우, 즉 새로운 문자의 시작
            _c = c # 현재 진행 중인 문자와 같지 않으므로 현재 진행 문자는 c로 대입
            if cnt: result += str(cnt) # 새로운 문자이므로 결과 문자열에 이전 문자의 카운트에 해당하는 값을 더해야 함
            
            result += c # 새로운 문자이므로 결과 문자열에 새로운 문자를 더함
            cnt = 1 # 새로운 문자이므로 카운트는 1로 초기화
        else: # 현재 진행중인 문자와 c가 같으므로 카운트 증가
            cnt += 1
    if cnt: result += str(cnt) # for loop를 벗어날 때 이전 문자의 카운트는 마지막으로 한 번 더해야 함
    
    return result # 최종 문자열 리턴

print(compress_string("aaabbcccccca")) # a3b2c6a1 출력
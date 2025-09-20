# Q1

def is_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
# Q2

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1, 2))
print(avg_numbers(1, 2, 3, 4, 5))

# Q3

input1 = input("첫 번째 숫자를 입력하세요: ")
input2 = input("두 번째 숫자를 입력하세요: ")

total = int(input1) + int(input2)
print("두 수의 합은 %s입니다." %total)

# Q4

# 3번, 쉼표는 공백이 생김

# Q5

# open으로 열 경우에는 무조건 close로 닫아줘야 한다.

# Q6

user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a')
f.write(user_input)
f.write('\n')
f.close()

# Q7

f = open('test.txt', 'r')
body = f.read()
f.close()
body = body.replace("java", "python")
f = open('test.txt', 'w')
f.write(body)
f.close()

# Q8

import sys

numbers = sys.argv[1:]

result = 0
for number in numbers:
    result +=int(number)
print(result)
    
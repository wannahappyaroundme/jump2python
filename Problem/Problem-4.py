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

# 3번
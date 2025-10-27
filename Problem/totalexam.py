# 1
# a:b:c:d -> a#b#c#d

text = "a:b:c:d" # text라는 변수에 a:b:c:d 문자열을 대입
A = text.split(":") # A라는 변수에 ":"를 기준으로 a, b, c, d로 나누고 리스트로 만듦
answer = "#".join(A) # join을 통해 A라는 리스트에 다시 #을 붙이고 문자열로 바꿈

print(answer)

# 2
# key에 해당하는 value를 출력하는 프로그램

a = {'A':90, 'B':80} # a라는 디렉토리에 A와 B라는 key에 90과 80이라는 value값을 각각 넣는다.
print(a.get('C', 70)) # a라는 디렉토리에 C가 없을 경우 none으로 이야기하지말고 70이라는 값을 배출하는 코드이다.

# 3
# Extend와 + [4, 5]의 차이

a = [1, 2, 3] # a라는 리스트에 1, 2, 3이라는 값을 선언
a = a + [4, 5] # 새로운 a라는 리스트를 만들어서 4, 5를 더한 새로운 1, 2, 3, 4, 5의 리스트 생성
a.append([4, 5]) # 기존 a라는 리스트에서 4, 5를 더해서 기존 리스트를 수정

# extend() = 원본 수정, +는 새 리스트 생성

# 4
# A학급 학생의 점수를 나타내는 리시트 다음 리스트에서 50점 이상 점수의 총합 

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25] # A라는 리스트에 값 입력
result = 0 # 총합인 result 변수 설정 초기화

for i in A: # A라는 집합의 i라는 값 사용하면서 계속 도는 반복문
    if i >= 50: # A 집합의 i라는 값이 50이 넘으면 아래 문장 실행 아니면 패스하는 조건문
        result += i #result에 i의 값을 더하고 저장
    
print(result) # 반복문이 다 끝난 뒤에 최종 result값 출력

# 5
# 피보나치 수열 만들기

def fibo(n): # n이라는 인자를 가진 fibo라는 함수 정의
    if n <= 0: # if n이 0보다 작을 때는 아래 문장 실행
        return [] # [] 빈 공백 출력
    elif n == 1: # if n이 1과 같을 때 아래 문장 실행
        return [0] # [0] 만 있는 내용 출력
    elif n == 2: # if n이 2과 같을 때 아래 문장 실행
        return [0, 1] # [0, 1] 만 있는 내용 출력
    result = [0, 1] # 위에 if문이 다 해당 되지 않을 때 result에 [0, 1] 입력 for 반복문에서 result[-1]과 result[-2]를 위해 있어야 함
    for i in range(n-2): # range의 숫자 동안 반복하는 반복문 이미 0, 1, 2의 사건이 있기에 2를 빼야 함
        next_num = result[-1]+result[-2] # next_num이라는 변수에 result에서 맨 뒤에 있는 숫자와 맨 뒤에서 2번째 있는 숫자의 합을 더 함
        result.append(next_num) # 그리고 result라는 리스트에서 next_num을 맨 뒤에 추가
    return result # 함수를 실행할 떄 result값을 반환
    
n = int(input("몇 항까지 출력할까요?")) # n이라는 변수에 입력 데이터를 넣고 그 입력 데이트를 정수로 변환하여 n에 대입 
print(fibo(n)) # fibo라는 함수의 n이라는 변수를 인자로 써서 출력

# 6 
# 숫자 총합 구하기

number = input("입력시킬 숫자를 적어주세요 :") # 입력할 데이터를 넣어서 number라는 변수에 저장
num2 = number.split(",") # 여러개의 숫자를 "," 사이로 구별 한 것 중 ","를 빼서 각각 하나씩 저장되는 상태로 만들고 num2에 저장
sum = 0 # 총합을 구하기 위해서 만든 sum이라는 변수에 0 초기값 셋팅
for i in num2: # for 반복문이고 input으로 받은 숫자를 split해서 리스트로 만들어 둔 것 중에 하나씩 i로 반복하는 문
    sum += int(i) # 총합을 구하기 위한 sum에 하나씩 정수로 더하기
    
print(sum) # for문이 끝나고 다 더 해진 sum을 출력해서 숫자 총합 확인

# 7
# 한 줄 구구단

gugudan = int(input("구구단을 출력할 숫자를 입력하세요(2~9):")) # gugudan이라는 변수에 정수로 입력 데이터를 받아서 저장
for i in range(1,10): # 1부터 시작해서 10번 총 1~9까지 반복하는 반복문
    dan = i * gugudan # dan이라는 변수에 i (1~9까지 올라가는 수) * input으로 들어온 값을 곱하기
    print(dan, end=" ") # 하나씩 출력하면서 end= " " 로 띄어쓰기를 만들어서 나열
print() # 마지막에 프린트를 통해서 맨 마지막 "%"기호 제거

# 8
# 파일 읽어서 역순으로 정하기
f = open('/Users/kyungsbook/Desktop/jump2python/Problem/abc.txt', 'r') # 같은 폴더에 절대 위치로 abc.txt를 읽음 상태로 파일 열어서 f라는 변수에 저장
lines = f.readlines() # f라는 변수에서 모든 줄들을 읽고 lines에 저장
f.close() # f라는 변수에 txt파일 열었던 것을 닫기 (open있을 때 무조건 close로 닫아야 함)

lines.reverse() # lines에 들어왔던 f변수에 있는 모든 줄들을 역순으로 재배열

f = open('/Users/kyungsbook/Desktop/jump2python/Problem/abc.txt', 'w') # 같은 폴더 절대위치에 있는 abc.txt를 쓰기 상태로 파일을 열어 f라는 변수에 다시 저장
for line in lines: # lines라는 abc.txt를 읽었던 파일들 중에서 line이라는 변수를 만듦
    line = line.strip() # strip을 통해 앞 뒤, 줄 빈칸을 모두 제거
    f.write(line) # f에다가 다시 line이라는 것을 한 줄씩 다시 적기
    f.write("\n") # \n을 통해 엔터 표시 줄 바꿈 표시를 넣음
f.close() # f를 다시 닫아서 abc.txt을 열어서 연동되었던 것을 끊음

# 9
# 평균값 구하기
f = open('/Users/kyungsbook/Desktop/jump2python/Problem/sample.txt', 'r') # 같은 폴더 절대 위치에 있는 sample.txt를 읽기 상태로 파일열어서 f라는 변수에 저장
lines = f.readlines() # f라는 변수에서 모든 줄들을 읽고 lines에 저장
f.close()  # f라는 변수에 txt파일 열었던 것을 닫기 (open있을 때 무조건 close로 닫아야 함)

total = 0 # 평균값 구하기 위해서 전체 숫자의 합을 구하기 위해 total 변수에 0 저장 초기값
for line in lines: # 저장된 lines에서 하나하나 line이라는 변수를 돌면서 반복
    total += int(line) # line을 int로 정수화 시키고 total 변수에 누적해서 저장
average = total /len(lines) # average에서 for문이 끝나고 total의 총합을 lines의 갯수로 나누어 평균을 구함

f = open('/Users/kyungsbook/Desktop/jump2python/Problem/result.txt', "w") # 같은 폴더 절대 위치에 있는 result.txt를 쓰기 상태로 파일을 열어 f에 변수 저장
f.write(str(average)) # 구한 average를 문자열로 바꾸고 f의 변수인 result.txt에 쓰기
f.close() # f를 다시 닫아서 연동된 result.txt를 끊기

# 10
# 계산기 만들기
class Calculator: # 계산기 클래스 선언
    def __init__(self, data): # 클래스 초기화 (data값고 셀프 값을 초기화로 설정)
        self.data = data # 데이터 값을 클래스의 값으로 저장
    
    def sum(self): # 더하기 함수를 만듦 값은 self로 받음
        result = 0 # 더하기 위한 result라는 변수에 0을 저장 초기화
        for d in self.data: # self.data에서 d라는 변수를 반복해서 실행할 반복문 제장
            result += d # 하나하나 d 값들을 result에 누적해서 저장
        return result # 함수가 끝나면 result값을 반환
    
    def avg(self): # 평균구하는 함수를 만들고 값은 self로 받음
        average = self.sum() / len(self.data) # average라는 변수에서 self에 sum()함수로 더하고 self.data라는 모든 값들의 길이로 평균을 구함
        return average # 함수가 끝나면 average값을 변환
    
    def multiply(self): # 모든 숫자를 곱하는 기능을 추가
        result = 1
        for m in self.data:
            result *= m
        return result

cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())
print(cal1.multiply())

cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.sum())
print(cal2.avg())        

# 11
# 모듈 사용하는 방법
import sys
sys.path.append("/Users/kyungsbook/Desktop/jump2python/Problem")
import mymod

# 12
# 오류와 예외 처리, 다음 코드의 실행 겨로가를 예측하고 그 이유를 설명하시오

result = 0 # result라는 변수에 초기값 0 대입

try: # try, except 구문 시작
    [1, 2, 3][3] # IndexError발생
    "a" + 1 # TypeError발생
    4 / 0 # ZeroDivisionError 발생
except TypeError: # TypeError가 발생할 경우 아래 구문을 실행
    result += 1 # result에 1을 더하기
except ZeroDivisionError: # ZeroDivisionError일 때는 아래 구문을 실행
    result += 2 # result에 2을 더하기
except IndexError: # IndexError일 때 아래 구문을 싱행, [1, 2, 3][3]이여서 IndexError이므로 아래 구문 실행
    result += 3 # result에 3을 더하기
finally: #맨 마지막에 무조건 아래 구문을 실행
    result += 4 # result에 4를 더하기
    
print(result) # indexError여서 3을 더하고 나머지 finally를 통해서 4를 더해 총 7의 값을 출력

# 13
# Dashinsert 함수

data = "4546793" # data라는 변수에 4546793이라는 문자열을 입력
numbers = list(map(int, data)) #data의 숫자 문자열을 정수로 바꾸고 각각 리스트로 바꿔서 numbers라는 변수에 저장 
result = [] #result를 빈 리스트로 선언하면서 저장
for i, num in enumerate(numbers): #numbers의 리스트 중에 i와 num이라는 변수를 반복하는 반복문
    result.append(str(num)) #result에 num이라는변수를 문자열로 바꿔서 더하기
    if i < len(numbers)-1: # numbers의 전체 길이보다 하나를 뺸 수보다 i가 적다면 밑에 구문 실행
        is_odd = num % 2 == 1 # num를 2로 나눴을 때 나머지가 1이 되는 경우 is_odd에 저장
        is_next_odd = numbers[i+1] % 2 == 1 # numbers에서 i가 아닌 다음 수를 2로 나눴을 떄 1이 남는 홀수일 경우에는 is_next_odd라고 저장
        if is_odd and is_next_odd: # 만약 is_odd과 is_next_odd 둘다 존재할 경우에는 
            result.append("-") # result 다음에 "-"을 입력할 것
        elif not is_odd and not is_next_odd: # 만약 is_odd와 is_next_odd 둘다 존재하지 않을 경우에는
            result.append("*") # result 다음에 "*"을 입력할 것
        
print("".join(result)) # result라는 리스트를 하나의 문자열로 만들고 "" <- 공백 없이 쭉 이어붙여서 출력 

# 14
# 문자가 연속적으로 반복되는 경우, 그 반복 횟수를 표시해서 문자열을 압축하여 표시하기
# 입력 예시 : aaabbcccccca, 출력 예시 : a3b2c6a1

def compress_string(s): # s라는 변수를 가지고 있는 compress_string이라는 함수 선언
    _c = "" # _c라는 변수에 빈 값을 저장 (초기값)
    cnt = 0 # cnt에 0이라는 숫자를 저장 (초기값)
    result = "" # 이 함수 최종 리턴 문자열 변수 선언 (초기값)
    for c in s: # 입력받은 문자열 s에서 c를 하나씩 대입하는 반복문
        if c != _c: # 입력 받은 문자와 _c값이 같지 않을 경우 아래 구문 실행
            _c = c # _c에 입력 받은 문자를 대입하여 같아지게 만듦
            if cnt: result += str(cnt) # 같지 않을 경우에는 cnt를 문자열로 해서 result에 더 함
            
            result += c # result에 c에 더하기
            cnt = 1 # cnt라는 변수에 1로 초기화
        else: # 현재 진행중인 문자와 c가 같을 경우 아래 구문을 진행
            cnt += 1 # cnt에게 1이라는 값을 더하기
    if cnt: result += str(cnt) # for 반복문이 끝날 때 한 번 더 cnt를 문자열로 해서 result에 더 함    
    return result # result 최종 문자열을 출력

print(compress_string("aaabbcccccca")) # a3b2c6a1 출력

# 15
# Duplicate Numbers 함수
# 0~9의 문자로 된 숫자를 입력받았을 떄 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.

def chk_dup_numbers(s): #s라는 데이터를 받아서 chk_dup_numbers 함수 실행
    result = [] # result에 빈 리스트를 정의
    for num in s: # 입력 받은 데이터 s에서 num라는 변수로 하나씩 가져오는 반복문 실행
        if num not in result: # num이라는 변수가 result안에 없을 경우, True로 아래 구문을 실행
            result.append(num) # result에 num를 리스트에 맨 뒤에 추가함
        else: # 그게 아니라면 아래 구문 실행
            return False # return에 false라는 것을 뱉음
    return len(result) == 10 # 함수가 끝날 때 result의 길이가 10일 때 True 아니면 false를 뱉음

print(chk_dup_numbers("0123456789")) # True 리턴
print(chk_dup_numbers("01234")) # False 리턴
print(chk_dup_numbers("01234567890")) # False 리턴
print(chk_dup_numbers("6789012345")) # True 리턴
print(chk_dup_numbers("012322456789")) # False 리턴

# 16
# 모스 부호 해독

dic = {
    '.-': 'A', '-...': 'B', '-.-': 'C', '-..':'D', '.' : 'E', '..-.': 'F', '--.': 'G', '....':'H', '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y', '--..':'Z'
} # 딕셔너리에서 모스 부호와 관련된 key값과 value값 설정 (초기값 설정)

def morse(src): # src라는 데이터를 받아서 실행하는 morse라는 함수 설정
    result = [] # result에 빈 리스트를 대입
    for word in src.split(" "): # src에서 띄어쓰기를 기준으로 하나씩 변수를 분리해서 리스트로 만든 것에서 word라는 변수로 하나씩 대입하는 반복문
        for char in word.split(" "): # word를 띄어쓰기를 기준으로 하나씩 또 변수를 분리해서 리스트를 만든 것에서 char라는 변수로 하나씩 대입하는 바놉ㄱ문
            result.append(dic[char]) # char이라는 변수의 char에 따라서 dic의 value값에 result 맨 뒤에 리스트에 추가하기 
        result.append(" ") # for 문이 끝나고 나면 띄어쓰기를 result 문자열에 더하기
    return "".join(result) # 띄어쓰기가 없이 result의 리스트를 하나의 문자열로 만들어서 함수가 끝날 때 반환하기

print(morse('.... . ... .-.. . . .--. ... . .- .-. .-.. -.--')) # H E S L E E P S E A R L Y

# 17
# 정규식 - 기초 메타 문자

import re # 정규식을 사용하기 위해 re 임포트
p = re.compile("a[.]{3,}b") # p라는 변수에 "a[.]{3,}b", a와 b사이에 "."이 최소 3개 이상있을 때 컴파일하는 값을 넣기

print(p.match("acccb")) # None
print(p.match("a....b")) # 매치 객체 출력
print(p.match("aaab")) # None
print(p.match("a.cccb")) # None

# 18
# 정규식 - 문자열 검색
import re # 정규식을 사용하기 위해 re 임포트

p = re.compile('[a-z]+') # p라는 변수에 "[a-z]+", a~z까지 소문자로만 이루어질 경우에는 컴파일을 한다고 선언
m = p.search("5 python") # p에 "5 python"에서 p의 compile하는 python만 출력해서 m에 대입
print(m.start() + m.end()) # python중에서 p와 n인 2와 8이 출력되어서 총 10이 출력

# 19
# 정규식 - 그루핑
import re # 정규식을 사용하기 위해 re 임포트

s = ''' 
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
''' # s라는 변수에 한 가지의 문자열이 아닌 여러 문자열을 '''을 이용해서 등록
pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}") # pat에 3개의 문자열과 사이 "-" 4개의 문자열 사이 "-"과 4개의 문자열을 설정
result2 = pat.sub("\g<1>-####", s) # 그 중에서 result2에 앞에 세트로 이어진 것을 빼고 뒤에 \d{4}부분만 ####로 변경한 뒤에 result2에 대입

print(result2) # result2을 출력 

# 20
# 정규식 - 전방 탐색

import re # 정규식을 사용하기 위해 re 임포트
pat = recompile(".*[@].*[.](?=com$|net$).*$") # pat에 '@'기준으로 전부 앞과 '.'기준으로 바로 앞에 추출하고 (?=)에서는 com이나 net인 경우에만 출력

print(pat.match("pahkey@gmail.com")) # 출력
print(pat.match("kim@daum.net")) # 출력
print(pat.match("lee@myhome.co.kr")) # none
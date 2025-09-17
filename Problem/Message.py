# \n 문자열 안에서 줄을 바꿀 때 사용
# \t 문자열 사이에 탭 간격을 줄 때 사용
# \\ | \' | \" : \,',"를 그대로 표현할 떄 사용
# \r 캐리지 리턴 (줄바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동)
# \f 폼 피드 (줄바꿈 문자, 커서를 현재 줄의 다음 줄로 이동)
# \a 벨 소리 (출력할 때 PC 스피커에서 "삑" 소리가 난다)
# \b 백 스페이스
# \000 Null 문자 

food = "Python's favorite food is perl"
say = '"Python is very easy." he says.'
food2 = 'Python\'s favorite food is perl'
say2 = "\"Python is very easy.\" he says."
multiline = "Life is too short\nYou need python"
multiline2 = '''
Life is too short
You need python
'''
a = "you need python"
b = "20250917Rainy"
year = b[:4]
day = b[4:8]
weather = b[8:]
number = 4
number2 = 10
day2 = "three"

# %s 문자열 (string)
# %c 문자 1개 (character)
# %d 정수 (integer)
# %f 부동소수 (floating-point)
# %o 8진수
# %x 16진수 # %% Literal % (문자 % 자체)

print("%10s" %"hi")
print("%-10sjane." %"hi")
print("%0.4f" %3.42134234)
print("%10.4f" %3.42134234)
print("I eat {0} apples.".format(3))
print("I eat {0} apples.".format("five"))
print("I ate %d apples. so i was sick for %s days." %(number2, day2))
print("I ate {number3} apples. so i was sick for {day3} days.".format(number3=8, day3="four"))
print("I eat %d apples." %number)
print("I eat %d apples." %3)
print("I eat %s apples." %"five")
print(food)
print(say)
print(food2)
print(say2)
print(multiline)
print(multiline2)
print(food+say)
print(say*3)
print(len(a))
print(day)
print(year)
print(weather)
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
print("{0:!>10}".format("hi"))
print("{0:!^10}".format("hi"))

y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))
print("{{and}}".format())

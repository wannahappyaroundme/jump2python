# Q1

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        
class UpgradedCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        
cal = UpgradedCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

# Q2

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

# Q3

print(all([1, 2, abs(-3)-3]))  # False
print(chr(ord('a')) == 'a')  # True

# Q4

print(list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3])))  # [1, 3, 8]

# Q5

hex(234)  # '0xea'
print(int('0xea', 16))  # 234

# Q6

print(list(map(lambda x: x*3, [1, 2, 3, 4])))  # [3, 6, 9, 12]

# Q7

a = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(a) + min(a))  # -1
a.sort()
print(a)  # [-8, -3, 0, 1, 2, 5, 5, 7]
print(a[0]+a[-1])  # -1


# Q8

print(round(17/3, 4))  # 5.6667

# Q9

import os

# os.chdir('C:/doit')
# result = os.popen('dir')
# print(result.read())

# Q10

import glob
print(glob.glob('C:/doit/*.py'))

# Q11

import time
print(time.strftime('%Y/%m/%d %H:%M:%S'))

# Q12

import random
print(random.sample(range(1, 46), 6))

# Q13

import datetime
sister = datetime.date(1995, 11, 20)
youngcheol = datetime.date(1998, 10, 6)

sub_day = youngcheol - sister

print(sub_day.days)  # 1051

# Q14

import operator

data = [('윤서현', 15.25), ('김예지', 13.31), ('박예원', 15.34), ('송순자', 15.57), ('김시우', 15.48), ('배숙자', 17.9), ('전정웅', 13.39), ('김혜진', 16.63), ('최보람', 17.14), ('한지영', 14.83), ('이성호', 17.7), ('김옥순', 16.71), ('황민지', 17.65), ('김영철', 16.7), ('주병철', 15.67), ('박상현', 14.16), ('김영순', 14.81), ('오지아', 15.13), ('윤지은', 16.93), ('문재호', 16.39)]

data = sorted(data, key=operator.itemgetter(1))

for i in data:
    print(i)

# Q15

import itertools

student = ['나지혜', '성성민', '윤지현', '김정숙']
result = itertools.combinations(student, 2)
print(list(result))

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
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

all([1, 2, abs(-3)-3])  # False
chr(ord('a')) == 'a'  # True

# Q4

list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3]))  # [1, 3, 8]

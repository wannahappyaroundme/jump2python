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

# 
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
        
    def mul(self):
        result = self.first * self.second
        return result
        
    def sub(self):
        result = self.first - self.second
        return result
        
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal()
print(type(a))
a.setdata(4, 2)
b = FourCal()
b.setdata(3, 8)
print(a.first)
print(a.second)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
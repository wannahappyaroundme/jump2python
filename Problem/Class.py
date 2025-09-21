class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
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
    
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0 :
            return 0
        else:
            return self.first / self.second

a = FourCal(4, 2)
print(type(a))
a.setdata(4, 2)
b = FourCal(3, 8)
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

c = MoreFourCal(4, 2)
print(c.add())
print(c.mul())
print(c.sub())
print(c.div())
print(c.pow())

d = SafeFourCal(4, 0)
print(d.div())

class Family:
    lastname = "김"
    
print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

Family.lastname = "박"
print(a.lastname)
print(b.lastname)

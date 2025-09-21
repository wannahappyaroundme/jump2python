class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = FourCal()
print(type(a))
a.setdata(4,2)
print(a.first)
print(a.second)
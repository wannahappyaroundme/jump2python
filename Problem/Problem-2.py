# Q1
Korea = 80
English = 75
Math = 55

Average = (Korea + English + Math)/3

print(Average)

# Q2

a = 13

if a // 2 == 0 :
    print("자연수 13은 짝수")
else:
    print("자연수 13은 홀수")
    
# Q3

pin = "881120-1068234"
yyyymmdd = "19" + pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# Q4

print(pin[7:8])

# Q5

d = "a:b:c:d"
e = d.replace(":", "#")
print(e)

# Q6

f = [1, 3, 5, 4, 2]
f.sort()
f.reverse()
print(f)

# Q7

g = ["Life", "is", "too", "short"]
result = " ".join(g)
print(result)

# Q8

h = (1, 2, 3)
h = h +(4,)
print(h)

# Q9

j = dict()
print(j)

# Q10

k = {'A' : 90, 'B' : 80, 'C' : 70}
result = k.pop('B')
print(k)
print(result)

# Q11

n = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
nSet = set(n)
m = list(nSet)
print(m)

# Q12

r = y = [1, 2, 3]
r[1] = 4
print(y)
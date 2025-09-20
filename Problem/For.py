test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
    
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)
    
b = range(10)
print(b)

c = range(1, 11)
print(c)

add = 0
for i in range(1, 11):
    add = add + i
print(add)
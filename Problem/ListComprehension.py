a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
    
print(result)

b = [2, 3, 4, 5]
result2 =[num*3 for num in b]
print(result2)

c = [3, 4, 5, 6]
result3 = [num*3 for num in c if num%2 == 0]
print(result3)
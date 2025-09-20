a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1, 2, 3]
print(a)
del a[1]
print(a)

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

d = {'a': 1, 'b': 2}
print(d['a'])
print(d['b'])

dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

dic.keys()
print(dic.keys())

for k in dic.keys():
    print(k)
    
list(dic.keys())
print(list(dic.keys()))

dic.items()
print(dic.items())
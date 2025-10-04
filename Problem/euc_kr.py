with open('euc_kr.txt', encoding='utf-8') as f:
    data = f.read()
    
data = data + '\n'

with open('euc_kr.txt', encoding='utf-8', mode='w') as f:
    f.write(data)
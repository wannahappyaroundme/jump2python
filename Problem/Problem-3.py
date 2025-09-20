# Q1

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else : print("none")

# Q2

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)

# Q3

j = 0
while True:
    j += 1
    if j > 5 : break
    print("*"*j)
    
#
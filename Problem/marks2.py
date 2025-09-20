marks = [90, 25, 67, 45, 80]

number = 0
for i in marks:
    number = number + 1
    if i < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %number)
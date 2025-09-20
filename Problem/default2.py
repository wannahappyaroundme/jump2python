def say_myself(name, man=True, age):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d살입니다." %age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
        
say_myself("박응용", 27)

# 초기화 하고 싶은 매개변수는 항상 맨 뒤쪽에 놓아야 한다! 잊지말 것
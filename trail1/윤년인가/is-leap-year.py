# 변수 선언, 입력
y = int(input())

# 출력
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print("true")
        else:
            print("false")
    else:
        print("true")
else:
    print("false")

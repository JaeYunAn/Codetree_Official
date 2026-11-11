math_A, eng_A = map(int, input().split())
math_B, eng_B = map(int, input().split())

if math_A > math_B:
    print('A')
elif math_B > math_A:
    print('B')

elif math_A == math_B:

    if eng_A > eng_B:
        print('A')
    elif eng_B > eng_A:
        print('B')
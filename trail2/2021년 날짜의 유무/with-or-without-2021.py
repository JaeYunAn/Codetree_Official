def f():
    M, D = map(int, input().split())
    if 1 <= M <= 12:
        if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
            if 1 <=  D <= 31:
                return 'Yes'
            else:
                return 'No'
        elif M == 4 or M == 6 or M == 9 or M == 11:
            if 1 <= D <= 30:
                return 'Yes'
            else:
                return 'No'
        elif M == 2:
            if 1 <= D <= 28:
                return 'Yes'
            else:
                return 'No'
    else:
        return 'No'
print(f())
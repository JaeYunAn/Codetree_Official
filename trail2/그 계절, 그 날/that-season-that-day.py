def f():
    Y, M, D = map(int, input().split())
    ymd = []
    if Y % 4 == 0 and (Y % 100 != 0 or Y % 400 == 0):
        if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
            if 1 <= D <= 31:
                ymd.append(Y)
                ymd.append(M)
                ymd.append(D)
            else:
                return -1
        elif M == 4 or M == 6 or M == 9 or M == 11:
            if 1 <= D <= 30:
                ymd.append(Y)
                ymd.append(M)
                ymd.append(D)
            else:
                return -1
        elif M == 2:
            if 1 <= D <= 29:
                ymd.append(Y)
                ymd.append(M)
                ymd.append(D)
            else:
                return -1
    else:
        if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
            if 1 <= D <= 31:
                ymd.append(Y)
                ymd.append(M)
                ymd.append(D)
            else:
                return -1
        elif M == 4 or M == 6 or M == 9 or M == 11:
            if 1 <= D <= 30:
                ymd.append(Y)
                ymd.append(M)
                ymd.append(D)
            else:
                return -1
        elif M == 2:
            if 1 <= D <= 28:
                ymd.append(Y)
                ymd.append(M)
                ymd.append(D)
            else:
                return -1

    if 3 <= ymd[1] <= 5:
        return 'Spring'
    elif 6 <= ymd[1] <= 8:
        return 'Summer'
    elif 9 <= ymd[1] <= 11:
        return 'Fall'
    elif ymd[1] == 12 or ymd[1] == 1 or ymd[1] == 2:
        return 'Winter'

print(f())
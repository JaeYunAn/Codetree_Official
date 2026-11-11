def f():
    An, Bn = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(An - Bn + 1):
        if A[i:i + Bn] == B:
            print('Yes')
            break
    else:
        print('No')
f()

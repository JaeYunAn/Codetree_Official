def make_fibo(n, m):
    fibo = []
    fibo.append(n)
    fibo.append(m)
    i = 1
    while i < 9:
        fibo.append((2*fibo[i - 1]) + fibo[i])
        i += 1
    return fibo

N, M = map(int, input().split())

fibo_real = make_fibo(N, M)
print(*fibo_real)
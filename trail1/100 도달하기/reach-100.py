def make_fibo(n):
    fibo = []
    fibo.append(1)
    fibo.append(n)
    i = 1
    while fibo[i] < 100:
        fibo.append(fibo[i - 1] + fibo[i])
        i += 1
    return fibo

N = int(input())

fibo_real = make_fibo(N)
print(*fibo_real)
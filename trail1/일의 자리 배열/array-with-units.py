def get_fibo(a, b):
    fibo = []
    fibo.append(a)
    fibo.append(b)

    for i in range(2, 10):
        fibo.append((fibo[i - 1] + fibo[i - 2]) % 10)

    return fibo

a, b = map(int, input().split())

fibo_real = get_fibo(a, b)
print(*fibo_real)
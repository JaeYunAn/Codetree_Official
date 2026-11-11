def f():
    N = int(input())
    N_sum = 0
    for i in range(1, N + 1):
        N_sum += i

    return N_sum // 10

print(f())
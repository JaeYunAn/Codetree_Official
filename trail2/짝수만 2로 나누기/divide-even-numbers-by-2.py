def f():
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N):
        if numbers[i] % 2 == 0:
            numbers[i] //= 2

    return print(*numbers)

f()
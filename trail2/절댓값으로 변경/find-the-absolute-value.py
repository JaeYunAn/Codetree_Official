def f():
    N = int(input())
    numbers = list(map(int, input().split()))

    numbers_new = []

    for i in numbers:
        numbers_new.append(abs(i))

    print(*numbers_new)

f()
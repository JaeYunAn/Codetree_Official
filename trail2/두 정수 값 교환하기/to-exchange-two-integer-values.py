def f():
    n, m = map(int, input().split())

    n, m = m, n

    return f'{n} {m}'

print(f())
def f(N):
    if N == 0:
        return
    print('HelloWorld')
    f(N - 1)

N = int(input())
f(N)
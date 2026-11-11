def f_1(N):
    if N == 0:
        return
    print(N, end = ' ')
    f_1(N - 1)

def f_2(N):
    if N == 0:
        return
    f_2(N - 1)
    print(N, end = ' ')
N = int(input())
f_2(N)
print()
f_1(N)
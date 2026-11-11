N = int(input())

def up(n, k):
    if n == k + 1:
        return
    print(n, end = ' ')
    up(n + 1, k)

def down(k, n):
    if n == 0:
        n += 1
        up(n, k)
        return
    print(n, end = ' ')
    down(k, n - 1)

down(N, N)
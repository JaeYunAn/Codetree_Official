K, N = map(int, input().split())
path = []

def perm(depth):
    if depth == N:
        print(*path)
        return

    for i in range(1, K + 1):
        path.append(i)
        perm(depth + 1)
        path.pop()
perm(0)
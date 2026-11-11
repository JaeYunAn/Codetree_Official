N, M = map(int, input().split())
A = list(map(int, input().split()))
Ms = [list(map(int, input().split())) for _ in range(M)]

def f():
    global N, M, A, Ms

    for i in range(M):
        print(sum(A[Ms[i][0]-1:Ms[i][1]]))
f()
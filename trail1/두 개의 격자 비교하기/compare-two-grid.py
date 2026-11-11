N, M = map(int, input().split())

matrix_1 = [list(map(int, input().split())) for _ in range(N)]
matrix_2 = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    matrix_3 = []
    for j in range(M):
        if matrix_1[i][j] == matrix_2[i][j]:
            matrix_3.append(0)
        else:
            matrix_3.append(1)
    print(*matrix_3)
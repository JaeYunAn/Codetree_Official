N, M = map(int, input().split())
matrix = [[0] * M for _ in range(N)]
number = 0

for j in range(M):
    for i in range(N):
        if j % 2 == 0:
            matrix[i][j] = number
            number += 1

        elif j % 2 == 1:
            matrix[N -1 - i][j] = number
            number += 1

for k in matrix:
    print(*k)
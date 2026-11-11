N, M = map(int, input().split())
matrix = [[0] * M for _ in range(N)]
number = 1

for d in range(N + M - 1):
    for i in range(N):
        j = d - i
        if 0 <= j < M:
            matrix[i][j] = number
            number += 1

for row in matrix:
    print(*row)
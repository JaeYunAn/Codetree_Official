N, M = map(int, input().split())

matrix = [[0] * M for _ in range(N)]

number = 0

for i in range(N):
    for j in range(M):
        number += 1
        matrix[i][j] = number
    print(*matrix[i])
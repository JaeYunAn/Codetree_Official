N = int(input())

matrix = [[1] * N for _ in range(N)]

for i in range(1, N):
    for j in range(1, N):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1] + matrix[i - 1][j - 1]

for row in matrix:
    print(*row)
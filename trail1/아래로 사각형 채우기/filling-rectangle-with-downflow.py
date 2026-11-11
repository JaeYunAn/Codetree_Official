N = int(input())

matrix = [[0] * N for _ in range(N)]

number = 1

for j in range(N):
    for i in range(N):
        matrix[i][j] = number
        number += 1

for i in range(N):
    print(*matrix[i])
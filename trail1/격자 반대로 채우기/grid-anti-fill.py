N = int(input())

matrix = [[0] * N for _ in range(N)]

number = 1

for j in range(N - 1, -1, -1):
    k = N - 1 - j
    for i in range(N):
        if k % 2 == 0:
            matrix[N - 1 - i][j] = number
            number += 1
        elif k % 2 == 1:
            matrix[i][j] = number
            number += 1

for row in matrix:
    print(*row)
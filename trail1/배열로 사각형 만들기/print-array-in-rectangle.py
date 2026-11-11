matrix = [[1] * 5 for _ in range(5)]

for i in range(1, 5):
    for j in range(1, 5):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

for row in matrix:
    print(*row)
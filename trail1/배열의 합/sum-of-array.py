matrix = [list(map(int, input().split())) for _ in range(4)]

for i in range(4):
    matrix_sum = 0
    for j in range(4):
        matrix_sum += matrix[i][j]
    print(matrix_sum)
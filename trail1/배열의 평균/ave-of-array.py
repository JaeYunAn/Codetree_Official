matrix = [list(map(int, input().split())) for _ in range(2)]

row_avg = []
col_avg = []

for i in range(2):
    row_sum = 0
    for j in range(4):
        row_sum += matrix[i][j]
    row_avg.append(row_sum / 4)
print(*[f'{x:.1f}' for x in row_avg])

for j in range(4):
    col_sum = 0
    for i in range(2):
        col_sum += matrix[i][j]
    col_avg.append(col_sum / 2)
print(*[f'{x:.1f}' for x in col_avg])

matrix_sum = 0
for i in range(2):
    for j in range(4):
        matrix_sum += matrix[i][j]
print(f'{matrix_sum / 8:.1f}')
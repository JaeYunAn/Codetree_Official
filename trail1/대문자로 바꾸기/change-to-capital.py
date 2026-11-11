matrix = [input().split() for _ in range(5)]

for i in range(5):
    row = []
    for j in range(3):
        row.append(matrix[i][j].upper())
    print(*row)
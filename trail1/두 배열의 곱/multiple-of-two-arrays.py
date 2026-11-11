matrix_1 = [list(map(int, input().split())) for _ in range(3)]
input()
matrix_2 = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    matrix_rhq = []
    for j in range(3):
        matrix_rhq.append(matrix_1[i][j] * matrix_2[i][j])
    print(*matrix_rhq)
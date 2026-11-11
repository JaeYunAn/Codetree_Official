N, M, K = map(int, input().split())
K -= 1
matrix = [list(map(int, input().split())) for _ in range(N)]
matrix.append([1] * N)
r = 0
c = K

while True:
    ni = r + 1

    blocked = False
    for j in range(M):
        if matrix[ni][c + j] == 1:
            blocked = True

    if blocked:
        break
    else:
        r = ni

for i in range(M):
    matrix[r][c + i] = 1

matrix.pop()

for row in matrix:
    print(*row)
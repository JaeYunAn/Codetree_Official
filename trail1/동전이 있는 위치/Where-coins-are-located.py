N, M = map(int, input().split())

r_list = []
c_list = []

rc_list = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    for j in range(2):
        if j == 0:
            r_list.append(rc_list[i][j] - 1)
        elif j == 1:
            c_list.append(rc_list[i][j] - 1)

matrix = [[0] * N for _ in range(N)]

for i in range(M):
    matrix[r_list[i]][c_list[i]] = 1

for row in matrix:
    print(*row)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

r -= 1
c -= 1

num_list = []
num_list.append(matrix[r][c])

while True:
    for d in range(4):
        ni = r + di[d]
        nj = c + dj[d]

        if 0 <= ni <= N - 1 and 0 <= nj <= N - 1 and matrix[ni][nj] > matrix[r][c]:
            r = ni
            c = nj
            num_list.append(matrix[r][c])
            break
    else:
        break
print(*num_list)
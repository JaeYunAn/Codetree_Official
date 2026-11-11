di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

k = 0

for i in matrix:
    if k < max(i):
        k = max(i)

K_list = [0] * (k + 1)

for K in range(1, k + 1):
    visited = [[0] * M for _ in range(N)]
    r, c = 0, 0
    count = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] > K and visited[i][j] == 0:
                r, c = i, j
                count += 1

                visited[r][c] = 1
                stack = []

                while True:
                    for d in range(4):
                        ni = r + di[d]
                        nj = c + dj[d]

                        if 0 <= ni <= N - 1 and 0 <= nj <= M - 1 and matrix[ni][nj] > K and visited[ni][nj] == 0:
                            stack.append((r, c))
                            r, c = ni, nj
                            visited[r][c] = 1
                            break
                    else:
                        if stack:
                            r, c = stack.pop()
                        else:
                            break
    K_list[K] = count
    
if max(K_list) == 0:
    print(f'1 0')
else:
    print(f'{K_list.index(max(K_list))} {max(K_list)}')
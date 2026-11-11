di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
count_list = []
max_size = 0

r, c = 0, 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 1:
            continue

        r, c = i, j
        visited[r][c] = 1
        count = 1
        stack = []

        while True:
            for d in range(4):
                ni = r + di[d]
                nj = c + dj[d]

                if 0 <= ni <= N - 1 and 0 <= nj <= N - 1 and matrix[ni][nj] == matrix[r][c] and visited[ni][nj] == 0:
                    stack.append((r, c))
                    r, c = ni, nj
                    visited[r][c] = 1
                    count += 1
                    break
            else:
                if stack:
                    r, c = stack.pop()
                else:
                    if count >= 4:
                        count_list.append(count)
                    if count > max_size:
                        max_size = count
                    break
                    
print(f'{len(count_list)} {max_size}')
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
start_list = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(N)]
count = 0

for r, c in start_list:
    r -= 1
    c -= 1

    q = deque()
    q.append((r, c))
    if visited[r][c] == 0:
        count += 1
    visited[r][c] = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            ni = r + di[d]
            nj = c + dj[d]

            if 0 <= ni <= N - 1 and 0 <= nj <= N - 1 and matrix[ni][nj] == 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                count += 1
print(count)
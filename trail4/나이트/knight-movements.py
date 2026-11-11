from collections import deque
di = [-2, -2, -1, -1, 1, 1, 2, 2]
dj = [-1, 1, -2, 2, -2, 2, -1, 1]

N = int(input())
knight = list(map(int, input().split()))

matrix = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
answer = -1

matrix[knight[2] - 1][knight[3] - 1] = 9
r = knight[0] - 1
c = knight[1] - 1

q = deque()
q.append((r, c))
visited[r][c] = 1

while q:
    r, c = q.popleft()

    if matrix[r][c] == 9:
        answer = visited[r][c] - 1

    for d in range(8):
        ni = r + di[d]
        nj = c + dj[d]

        if 0 <= ni <= N - 1 and 0 <= nj <= N - 1 and visited[ni][nj] == 0:
            q.append((ni, nj))
            visited[ni][nj] = visited[r][c] + 1
print(answer)
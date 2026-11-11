from collections import deque
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
answer = 0
r, c = 0, 0

q = deque()
q.append((r, c))
visited[r][c] = 1

while q:
    r, c = q.popleft()
    
    if r == N - 1 and c == M - 1:
        answer = 1
    
    for d in range(4):
        ni = r + di[d]
        nj = c + dj[d]
        
        if 0 <= ni <= N - 1 and 0 <= nj <= M - 1 and matrix[ni][nj] == 1 and visited[ni][nj] == 0:
            q.append((ni, nj))
            visited[ni][nj] = 1

print(answer)
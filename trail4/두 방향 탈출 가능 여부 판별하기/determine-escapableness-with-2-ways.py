di = [1, 0]
dj = [0, 1]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

answer = 0
r = 0
c = 0

visited = [[0] * M for _ in range(N)]
stack = []
visited[r][c] = 1

while True:
    for d in range(2):
        ni = r + di[d]
        nj = c + dj[d]

        if 0 <= ni <= N - 1 and 0 <= nj <= M - 1 and matrix[ni][nj] == 1 and visited[ni][nj] == 0:
            stack.append((r, c))
            r = ni
            c = nj
            visited[r][c] = 1

            if r == N - 1 and c == M - 1:
                answer = 1
            break
    else:
        if stack:
            r, c = stack.pop()
        else:
            break
print(answer)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
count_list = []
r = 0
c = 0

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            r, c = i, j
            visited[r][c] = 1
            stack = []
            count = 1

            while True:
                for d in range(4):
                    ni = r + di[d]
                    nj = c + dj[d]

                    if 0 <= ni <= N - 1 and 0 <= nj <= N - 1 and matrix[ni][nj] == 1 and visited[ni][nj] == 0:
                        stack.append((r, c))
                        r, c = ni, nj
                        visited[r][c] = 1
                        count += 1
                        break
                else:
                    if stack:
                        r, c = stack.pop()
                    else:
                        count_list.append(count)
                        break
count_list.sort()
print(len(count_list))
for i in count_list:
    print(i)
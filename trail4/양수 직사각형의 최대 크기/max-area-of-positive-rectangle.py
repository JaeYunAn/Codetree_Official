N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

answer = -1

for x1 in range(N):
    for y1 in range(M):
        for x2 in range(x1, N):
            for y2 in range(y1, M):
                ok = True
                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        if matrix[i][j] <= 0:
                            ok = False

                if ok:
                    size = (x2 - x1 + 1) * (y2 - y1 + 1)
                    if size > answer:
                        answer = size
print(answer)
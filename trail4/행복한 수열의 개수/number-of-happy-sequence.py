N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N - M + 1):
        for k in range(M):
            if matrix[i][j] != matrix[i][j + k]:
                break
        else:
            count += 1
            break

for j in range(N):
    for i in range(N - M + 1):
        for k in range(M):
            if matrix[i][j] != matrix[i + k][j]:
                break
        else:
            count += 1
            break
print(count)
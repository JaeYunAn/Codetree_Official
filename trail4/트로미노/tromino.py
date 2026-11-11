N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

count_list = []

for i in range(N):
    for j in range(M - 3 + 1):
        count = 0
        for k in range(3):
            count += matrix[i][j + k]
        count_list.append(count)

for i in range(N - 3 + 1):
    for j in range(M):
        count = 0
        for k in range(3):
            count += matrix[i + k][j]
        count_list.append(count)

for i in range(N - 2 + 1):
    for j in range(M - 2 + 1):
        count = 0
        for k in range(2):
            for L in range(2):
                count += matrix[i + k][j + L]

        for k in range(2):
            for L in range(2):
                count_list.append(count - matrix[i + k][j + L])

print(max(count_list))
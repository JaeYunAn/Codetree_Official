N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

count_list = []

for i in range(N - 3 + 1):
    for j in range(N - 3 + 1):
        count = 0
        for k in range(3):
            for L in range(3):
                if matrix[i + k][j + L] == 1:
                    count += 1
                    count_list.append(count)
print(max(count_list))
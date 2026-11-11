N = int(input())
triangle = [[1] * i for i in range(1, N + 1)]

for i in range(2, N):
    for j in range(1, i):
        triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

for row in triangle:
    print(*row)
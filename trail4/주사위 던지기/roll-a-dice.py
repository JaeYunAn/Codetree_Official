N, M, r, c = map(int, input().split())
go = list(input().split())
r -= 1
c -= 1
matrix = [[0] * N for _ in range(N)]
up = 1
down = 6
front = 2
back = 5
left = 4
right = 3
matrix[r][c] = down

for i in go:
    if i == 'L':
        if c - 1 < 0:
            continue
        else:
            c -= 1
            up, right, down, left = right, down, left, up

    elif i == 'R':
        if c + 1 > N - 1:
            continue
        else:
            c += 1
            up, right, down, left = left, up, right, down

    elif i == 'U':
        if r - 1 < 0:
            continue
        else:
            r -= 1
            up, front, down, back = front, down, back, up

    elif i == 'D':
        if r + 1 > N - 1:
            continue
        else:
            r += 1
            up, front, down, back = back, up, front, down
    matrix[r][c] = down
    
matrix_sum = 0

for i in matrix:
    for j in i:
        matrix_sum += j

print(matrix_sum)
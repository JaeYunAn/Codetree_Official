N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
count = 0
for i in range(N):
    point_sum = 0
    for j in range(4):
        point_sum += matrix[i][j]
    if point_sum / 4 >= 60:
        print('pass')
        count += 1
    else:
        print('fail')

print(count)
def make_square(N):
    number = 1
    square = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            square[i][j] = number % 10
            number += 1
            if number % 10 == 0:
                number += 1
    return square

N = int(input())

for row in make_square(N):
    print(*row)
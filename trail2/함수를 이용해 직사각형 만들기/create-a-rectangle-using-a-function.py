def make_square(n, m):
    square = [['1'] * m for _ in range(n)]
    return square
n, m = map(int, input().split())

for row in make_square(n, m):
    print(''.join(row))
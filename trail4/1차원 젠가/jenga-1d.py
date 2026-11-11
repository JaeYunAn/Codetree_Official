N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
first = list(map(int, input().split()))
second = list(map(int, input().split()))

new_matrix = []

for i in matrix:
    for j in i:
        new_matrix.append(j)

for i in range(first[0] - 1, first[1]):
    new_matrix[i] = 0

count = 0
for i in range(N):
    if new_matrix[i] != 0:
        count += 1
        if second[0] <= count <= second[1]:
            new_matrix[i] = 0

new_count = 0
for i in new_matrix:
    if i != 0:
        new_count += 1
print(new_count)

for i in new_matrix:
    if i != 0:
        print(i)
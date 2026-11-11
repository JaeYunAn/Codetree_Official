n = int(input())
a = list(map(int, input().split()))

count = 0
min_num = a[0]

for i in a:
    if i < min_num:
        min_num = i

for j in a:
    if j == min_num:
        count += 1

print(min_num, count)
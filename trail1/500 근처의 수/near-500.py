numbers = list(map(int, input().split()))

under_500 = []
over_500 = []

for i in numbers:
    if i < 500:
        under_500.append(i)
    else:
        over_500.append(i)

max_num = under_500[0]
min_num = over_500[0]

for j in under_500:
    if j > max_num:
        max_num = j

for k in over_500:
    if k < min_num:
        min_num = k

print(max_num, min_num)
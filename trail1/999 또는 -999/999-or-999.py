numbers = list(map(int, input().split()))

numbers_new = []

for i in numbers:
    if -999 < i < 999:
        numbers_new.append(i)

max_num = numbers_new[0]
min_num = numbers_new[0]

for j in numbers_new:
    if j > max_num:
        max_num = j
    elif j < min_num:
        min_num = j

print(max_num, min_num)
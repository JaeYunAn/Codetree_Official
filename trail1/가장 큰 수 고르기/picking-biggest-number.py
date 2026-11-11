numbers = list(map(int, input().split()))

max_num = numbers[0]

for i in numbers:
    if i > max_num:
        max_num = i
print(max_num)
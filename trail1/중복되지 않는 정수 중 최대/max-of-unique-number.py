N = int(input())

numbers = list(map(int, input().split()))

numbers_count = [0] * 1000
numbers_new = []

for i in range(N):
    numbers_count[numbers[i] - 1] += 1

for j in range(len(numbers_count)):
    if numbers_count[j] == 1:
        numbers_new.append(j + 1)

if not numbers_new:
    print(-1)
else:
    max_num = numbers_new[0]

    for k in numbers_new:
        if k > max_num:
            max_num = k
    print(max_num)
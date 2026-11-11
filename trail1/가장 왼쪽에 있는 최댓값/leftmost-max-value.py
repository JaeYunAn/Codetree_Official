N = int(input())

numbers = list(map(int, input().split()))

max_idx_list = []
max_num = numbers[0]

for i in range(N):
    if numbers[i] > max_num:
        max_num = numbers[i]
max_idx_list.append(numbers.index(max_num))

for j in range(N):
    end = max_idx_list[-1]
    if end == 0:
        break
    max_num_2 = numbers[0]
    for k in range(end):
        if numbers[k] > max_num_2:
            max_num_2 = numbers[k]
    max_idx_list.append(numbers.index(max_num_2))

print(*[idx + 1 for idx in max_idx_list])
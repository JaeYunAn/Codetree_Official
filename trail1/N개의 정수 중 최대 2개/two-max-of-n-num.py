N = int(input())

numbers = list(map(int, input().split()))

max_list = []

for i in range(2):
    max_num = numbers[0]
    for j in range(N):
        if numbers[j] > max_num:
            max_num = numbers[j]
    max_list.append(max_num)
    numbers[numbers.index(max_num)] = float('-inf')

print(*max_list)
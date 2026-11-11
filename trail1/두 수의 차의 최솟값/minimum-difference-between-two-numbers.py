N = int(input())

numbers = list(map(int, input().split()))

min_num = float('inf')

for i in range(N):
    for j in range(i + 1, N):
        if numbers[j] - numbers[i] < min_num:
            min_num = numbers[j] - numbers[i]
print(min_num)
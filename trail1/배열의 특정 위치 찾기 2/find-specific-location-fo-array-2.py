numbers = list(map(int, input().split()))

num_sum = 0
num_sum_sum = 0

for i in range(len(numbers)):
    if i % 2 == 0:
        num_sum += numbers[i]
    else:
        num_sum_sum += numbers[i]

print(abs(num_sum - num_sum_sum))
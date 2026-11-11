numbers = list(map(int, input().split()))

numbers_sum = 0
numbers_sum_2 = 0

for i in range(len(numbers)):
    if i % 2 == 1:
        numbers_sum += numbers[i]

for j in range(len(numbers)):
    if j == 2 or j == 5 or j == 8:
        numbers_sum_2 += numbers[j]

numbers_avg = numbers_sum_2 / 3

print(f'{numbers_sum} {numbers_avg:.1f}')
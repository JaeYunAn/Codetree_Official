numbers = list(map(int, input().split()))
numbers_sum = 0
for i in range(10):
    if i == 2 or i == 4 or i == 9:
        numbers_sum += numbers[i]
print(numbers_sum)
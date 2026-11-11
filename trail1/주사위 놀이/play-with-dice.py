dice = list(map(int, input().split()))

numbers_list = [0] * 6

for i in dice:
    numbers_list[i - 1] += 1

for j in range(6):
    print(f'{j + 1} - {numbers_list[j]}')
numbers = list(map(int, input().split()))
numbers_new = []
numbers_new_new = []
numbers_list = [0] * 9

for i in numbers:
    if i == 0:
        break
    elif i >= 10:
        numbers_new.append(i)

for j in numbers_new:
    numbers_new_new.append(j // 10)

for k in numbers_new_new:
    numbers_list[k - 1] += 1


for L in range(len(numbers_list)):
    print(f'{L + 1} - {numbers_list[L]}')
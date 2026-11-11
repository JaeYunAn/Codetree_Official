numbers = list(map(int, input().split()))


numbers_new = []

for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers_new.append(numbers[i])
    else:
        break

for j in range(len(numbers_new)):
    if numbers_new[j] % 2 == 1:
        numbers_new[j] += 3
    else:
        numbers_new[j] //= 2

print(*numbers_new)
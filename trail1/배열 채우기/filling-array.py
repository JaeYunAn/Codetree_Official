numbers = list(map(int, input().split()))

numbers_new = []

for i in numbers:
    if i > 0:
        numbers_new.append(i)
    else:
        break
numbers_new_reverse = numbers_new[::-1]
print(*numbers_new_reverse)
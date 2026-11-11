numbers = list(map(int, input().split()))

numbers_new = []

for i in numbers:
    if i > 0:
        numbers_new.append(i)
    else:
        break

print(f'{sum(numbers_new)} {(sum(numbers_new) / len(numbers_new)):.1f}')
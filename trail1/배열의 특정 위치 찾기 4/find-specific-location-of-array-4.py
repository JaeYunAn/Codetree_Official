numbers = list(map(int, input().split()))

numbers_new = []

for i in numbers:
    if i > 0:
        numbers_new.append(i)
    else:
        break
        
numbers_new_new = []
count = 0

for i in numbers_new:
    if i % 2 == 0:
        count += 1
        numbers_new_new.append(i)

print(f'{count} {sum(numbers_new_new)}')
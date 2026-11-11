N = int(input())

numbers = list(map(int, input().split()))

numbers_new = []

for i in numbers:
    if i % 2 == 0:
        numbers_new.append(i)
print(*numbers_new)
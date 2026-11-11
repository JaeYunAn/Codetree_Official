N = int(input())
numbers = list(map(int, input().split()))
numbers_new = []

for i in numbers:
    numbers_new.append(i ** 2)
print(*numbers_new)
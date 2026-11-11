N, M = map(int, input().split())

numbers = list(map(int, input().split()))
count = 0
for i in numbers:
    if i == M:
        count += 1
print(count)
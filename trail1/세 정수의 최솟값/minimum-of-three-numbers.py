numbers = list(map(int, input().split()))

min_v = numbers[0]

for i in numbers:
    if i < min_v:
        min_v = i

print(min_v)
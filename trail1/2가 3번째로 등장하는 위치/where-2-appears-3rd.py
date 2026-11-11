N = int(input())

numbers = list(map(int, input().split()))

count = 0

for i in range(N):
    if numbers[i] == 2:
        count += 1
        if count == 3:
            print(i + 1)
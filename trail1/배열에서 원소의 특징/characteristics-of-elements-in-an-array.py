numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    if numbers[i] % 3 == 0:
        print(numbers[i - 1])
        break
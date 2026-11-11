numbers = list(map(int, input().split()))

if numbers[0] == min(numbers):
    print(1, end = ' ')
else:
    print(0, end = ' ')

if numbers[0] == numbers[1] == numbers[2]:
    print(1, end = ' ')
else:
    print(0, end = ' ')
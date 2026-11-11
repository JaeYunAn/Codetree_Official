N = int(input())

numbers = list(map(int, input().split()))

numbers_list = [0] * 9

for i in numbers:
    numbers_list[i - 1] += 1

for j in numbers_list:
    print(j)
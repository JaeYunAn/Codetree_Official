N = int(input())

numbers = [int(input()) for _ in range(N)]

numbers_sum = str(sum(numbers))

print(numbers_sum[1:] + numbers_sum[0])
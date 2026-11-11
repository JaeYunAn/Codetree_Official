N, T = map(int, input().split())
number_1 = list(map(int, input().split()))
number_2 = list(map(int, input().split()))

numbers = number_1 + number_2

for i in range(T):
    numbers = [numbers[-1]] + numbers[:-1]

print(*numbers[:N])
print(*numbers[N:])
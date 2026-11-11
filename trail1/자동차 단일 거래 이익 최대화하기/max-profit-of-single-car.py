N = int(input())

price = list(map(int, input().split()))

max_margin = 0

for i in range(N):
    for j in range(i + 1, N):
        if price[j] - price[i] > max_margin:
            max_margin = price[j] - price[i]

print(max_margin)
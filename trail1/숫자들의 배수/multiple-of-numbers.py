N = int(input())
arr = []
count = 0
i = 1

while count < 2:
    arr.append(N * i)
    if (N * i) % 5 == 0:
        count += 1
    i += 1
print(*arr)
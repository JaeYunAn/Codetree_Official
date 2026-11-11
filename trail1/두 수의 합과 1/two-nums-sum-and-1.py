a, b = map(int, input().split())

c = str(a + b)

count = 0

for i in c:
    if i == '1':
        count += 1
print(count)
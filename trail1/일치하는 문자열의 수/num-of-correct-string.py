n, A = input().split()
n = int(n)

text_list = [input() for _ in range(n)]
count = 0
for i in text_list:
    if i == A:
        count += 1
print(count)
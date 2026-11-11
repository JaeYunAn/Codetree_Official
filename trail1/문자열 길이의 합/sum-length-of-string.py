N = int(input())

text = [input() for _ in range(N)]

text_len_sum = 0
count = 0

for i in text:
    text_len_sum += len(i)
    if i[0] == 'a':
        count += 1
print(text_len_sum, count)
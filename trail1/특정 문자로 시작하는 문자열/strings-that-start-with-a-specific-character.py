N = int(input())
text = [input() for _ in range(N)]
char = input()

count = 0
text_list = []

for i in text:
    if char == i[0]:
        count += 1
        text_list.append(i)

text_sum = 0
for j in text_list:
    text_sum += len(j)

print(f'{count} {(text_sum / len(text_list)):.2f}')
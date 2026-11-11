text = input()

count_1 = 0
count_2 = 0

for i in range(len(text) - 1):
    if text[i] == 'e' and text[i + 1] == 'e':
        count_1 += 1

    elif text[i] == 'e' and text[i + 1] == 'b':
        count_2 += 1

print(f'{count_1} {count_2}')
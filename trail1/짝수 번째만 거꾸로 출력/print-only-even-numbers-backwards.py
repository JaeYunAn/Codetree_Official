text = input()

text_new = []

for i in range(len(text)):
    if i % 2 == 1:
        text_new.append(text[i])

print(''.join(text_new[::-1]))
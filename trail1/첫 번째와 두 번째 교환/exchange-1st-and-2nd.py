text = list(input())

for i in range(2, len(text)):
    if text[i] == text[0]:
        text[i] = text[1]
    elif text[i] == text[1]:
        text[i] = text[0]

text[0], text[1] = text[1], text[0]
print(''.join(text))
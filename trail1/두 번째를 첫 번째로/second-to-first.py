text = list(input())
char = text[1]
for i in range(len(text)):
    if text[i] == char:
        text[i] = text[0]
print(''.join(text))
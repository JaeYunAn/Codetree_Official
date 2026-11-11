text = input().split()

text_new = []

for i in range(len(text)):
    if i == 1 or i == 4 or i == 7:
        text_new.append(text[i])

print(*text_new)
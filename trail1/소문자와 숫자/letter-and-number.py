text = input()
text_new = ''

for i in text:
    if i.isalpha():
        text_new += i
    elif i.isdigit():
        text_new += i

print(text_new.lower())
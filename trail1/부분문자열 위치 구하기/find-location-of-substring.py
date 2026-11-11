text = input()
text_1 = input()

if text_1 in text:
    print(text.index(text_1))
else:
    print(-1)
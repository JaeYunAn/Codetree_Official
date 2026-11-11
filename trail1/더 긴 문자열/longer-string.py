text_1, text_2 = input().split()

if len(text_1) > len(text_2):
    print(text_1, len(text_1))
elif len(text_1) < len(text_2):
    print(text_2, len(text_2))
else:
    print('same')
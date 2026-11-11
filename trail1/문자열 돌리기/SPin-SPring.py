text = input()
print(text)
L = len(text)
i = 1
while i < L + 1:

    text = text[-1] + text[:-1]
    print(text)
    i += 1
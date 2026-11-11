text, char = input().split()

if char in text:
    print(text.index(char))
else:
    print('No')
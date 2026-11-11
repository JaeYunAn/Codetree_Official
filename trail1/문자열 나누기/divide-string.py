N = int(input())
text = ''.join(list(input().split()))
for i in range(0, len(text), 5):
    print(text[i:i + 5])
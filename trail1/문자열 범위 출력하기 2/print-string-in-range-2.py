text = input()
N = int(input())
text_reverse = []

if N > len(text):
    print(text[::-1])
else:
    for i in range(N):
        text_reverse.append(text[::-1][i])

    print(''.join(text_reverse))
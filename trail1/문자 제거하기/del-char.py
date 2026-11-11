text = list(input())

while True:

    N = int(input())

    if N <= len(text) - 1:
        text.pop(N)
        print(''.join(text))

    elif N >= len(text):
        text.pop(-1)
        print(''.join(text))

    if len(text) == 1:
        break
text, Q = input().split()
Q = int(Q)
quest = [int(input()) for _ in range(Q)]

for i in range(len(quest)):
    if quest[i] == 1:
        text = text[1:] + text[0]
        print(text)

    elif quest[i] == 2:
        text = text[-1] + text[:-1]
        print(text)

    elif quest[i] == 3:
        text = text[::-1]
        print(text)
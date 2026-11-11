from collections import deque

que = deque()

text = input()

for i in text:
    que.append(i)

t = que.popleft()
que.append(t)

print(''.join(que))
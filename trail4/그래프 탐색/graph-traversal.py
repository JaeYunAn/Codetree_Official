N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(M)]

adj_list = [[] for _ in range(N + 1)]

for i in range(M):
    s = G[i][0]
    e = G[i][1]

    adj_list[s].append(e)
    adj_list[e].append(s)

visited = [0] * (N + 1)
stack = []
s = 1
v = s
visited[v] = 1
count = 0

while True:
    for w in adj_list[v]:
        if visited[w] == 0:
            stack.append(v)
            v = w
            visited[v] = 1
            count += 1
            break
    else:
        if stack:
            v = stack.pop()
        else:
            break

print(count)
S, Q = input().split()
S = list(S)
Q = int(Q)
arr = [input().split() for _ in range(Q)]

for i in range(Q):

    if arr[i][0] == '1':
        S[int(arr[i][1]) - 1], S[int(arr[i][2]) - 1] = S[int(arr[i][2]) - 1], S[int(arr[i][1]) - 1]
    
    elif arr[i][0] == '2':
        for j in range(len(S)):
            if S[j] == arr[i][1]:
                S[j] = arr[i][2]
    print(''.join(S))
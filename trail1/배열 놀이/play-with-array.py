N, Q = map(int, input().split())
arr = list(map(int, input().split()))
Q_arr = [list(map(int, input().split())) for _ in range(Q)]
a_list = []

for i in range(Q):
    if Q_arr[i][0] == 1:
        print(arr[Q_arr[i][1] - 1])

    elif Q_arr[i][0] == 2:
        for j in range(N):
            if Q_arr[i][1] == arr[j]:
                print(j + 1)
                break
        else:
            print(0)

    elif Q_arr[i][0] == 3:
        a_list = []
        for k in range(Q_arr[i][1] - 1, Q_arr[i][2]):
            a_list.append(arr[k])
        print(*a_list)
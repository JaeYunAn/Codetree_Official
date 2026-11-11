N, M = map(int, input().split())
A = list(map(int, input().split()))
A_sum = 0
M_list = []
M_list.append(M)

def f():
    global N, M, A, M_list, A_sum
    while True:
        if M == 1:
            break

        elif M % 2 == 1:
            M -= 1
            M_list.append(M)

        elif M % 2 == 0:
            M //= 2
            M_list.append(M)
            if M == 1:
                break
    for i in M_list:
        A_sum += A[i - 1]
    return A_sum
print(f())

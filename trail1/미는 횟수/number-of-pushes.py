N = 0
A = input()
B = input()

while True:
    A = A[-1] + A[0:-1]
    N += 1

    if A == B:
        print(N)
        break

    if N == len(B):
        print(-1)
        break
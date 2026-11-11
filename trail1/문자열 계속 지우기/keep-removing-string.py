A = input()
B = input()

while True:
    idx = A.find(B)

    if idx == -1:
        print(A)
        break

    A = A[:idx] + A[idx + len(B):]

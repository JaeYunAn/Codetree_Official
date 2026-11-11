A = input()
B = input()

count = 0

for i in range(len(A) - 1):
    if A[i] == B[0] and A[i + 1] == B[1]:
        count += 1
print(count)
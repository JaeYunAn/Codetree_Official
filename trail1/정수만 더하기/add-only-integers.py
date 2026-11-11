A = input()

A_new = []

for i in A:
    if i.isdigit():
        A_new.append(int(i))

A_new_sum = 0
for i in A_new:
    A_new_sum += i

print(A_new_sum)
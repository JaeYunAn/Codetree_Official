A, B = input().split()
a = ''
b = ''

for i in A:
    if i.isdigit():
        a += i
    else:
        break

for i in B:
    if i.isdigit():
        b += i
    else:
        break

a = int(a)
b = int(b)

print(a + b)
A = input()
B = input()
a = ''
b = ''

for i in A:
    if i.isdigit():
        a += i
a = int(a)

for i in B:
    if i.isdigit():
        b += i
b = int(b)

print(a + b)
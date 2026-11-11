numbers = list(map(int, input().split()))
chars = []
for i in numbers:
    chars.append(chr(i))
print(*chars)
text = input()
alphabet = input()

count = 0
for i in text:
    if i == alphabet:
        count += 1
print(count)
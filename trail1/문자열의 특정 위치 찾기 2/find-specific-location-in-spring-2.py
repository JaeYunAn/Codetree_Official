text = ["apple", "banana", "grape", "blueberry", "orange"]

char = input()
count = 0
for i in text:
    if char == i[2] or char == i[3]:
        count += 1
        print(i)

print(count)
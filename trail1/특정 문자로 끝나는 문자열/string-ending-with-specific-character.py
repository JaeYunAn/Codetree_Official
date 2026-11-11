text = [input() for _ in range(11)]
count = 0
for i in text[0:10]:
    if text[-1] == i[-1]:
        print(i)
        count += 1

if count == 0:
    print('None')
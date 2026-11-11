text_list = []
while True:
    text = input()
    text_list.append(text)

    if text == '0':
        break

print(len(text_list) - 1)

for i in range(len(text_list) - 1):
    if i % 2 == 0:
        print(text_list[i])